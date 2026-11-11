
import pytest
from pages.technologies import technology


@pytest.mark.smoke
def test_ecommercedevelopment(page):
    technologyobject_obj = technology(page)
    technologyobject_obj.ecommerce_options_click()
    
@pytest.mark.smoke
def test_mobileappdevelopment(page):
    technologyobject_obj=technology(page)
    technologyobject_obj. mobileappdevelopment_options_click()

@pytest.mark.smoke
def test_artificialIntelligenc(page):
    technologyobject_obj=technology(page)
    technologyobject_obj.artificialIntelligence_options_click()