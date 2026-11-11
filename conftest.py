import base64
from pathlib import Path

import pytest
from playwright.sync_api import sync_playwright
from pytest_html import extras

from config import BASE_URL


@pytest.fixture(scope="function")
def page(request):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)

        recordings_dir = Path("recordings")
        recordings_dir.mkdir(exist_ok=True)
        context = browser.new_context(record_video_dir=str(recordings_dir))

        page = context.new_page()
        page.goto(BASE_URL)

        yield page

        video = page.video
        context.close()
        if video:
            request.node.video_path = Path(video.path())
        browser.close()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    extra = list(getattr(report, "extras", []))

    if report.when == "call" and report.failed:
        page = item.funcargs.get("page")

        if page:
            screenshots_dir = Path("screenshots")
            screenshots_dir.mkdir(exist_ok=True)

            file_name = screenshots_dir / f"{item.name}.png"
            page.screenshot(path=str(file_name))
            extra.append(extras.image(str(file_name)))

    if report.when == "teardown":
        video_file = getattr(item, "video_path", None)
        if isinstance(video_file, str):
            video_file = Path(video_file)

        if video_file and video_file.exists() and video_file.is_file():
            encoded_video = base64.b64encode(video_file.read_bytes()).decode("ascii")
            extra.append(extras.video(encoded_video, name=f"{item.name} session recording"))

    report.extras = extra