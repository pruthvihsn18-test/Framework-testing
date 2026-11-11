class vertical:

    def __init__(self, page): ####defining the constructor
        self.page=page
        ##vertical locator

        self.verticals=page.locator('(//li[@class="drop_down"])[1]') ####hover()

        self.trading= page.locator('//li[@data-id="trading"]')###trading tab
        self.Retail_Ecommerce= page.locator('//li[@data-id="retailEcommerce"]')##retaile
        self.Healthcare=page.locator('//li[@data-id="healthcare"]')
        self.Fintech= page.locator('//li[@data-id="fintech"]')
        self.customApp= page.locator('//li[@data-id="customApp"]')

        ###submenus of Trading tab
        self.p0=page.locator('(//li/a[@href="https://www.tranktechnologies.com/stock-trading-mobile-app-development-company"])[1]')
        self.p1=page.locator('(//li/a[@href="https://www.tranktechnologies.com/paper-trading-app-development-company"])[1]')
        self.p2=page.locator('(//li/a[@href="https://www.tranktechnologies.com/cfd-trading-app-development-company"])[1]')
        self.p3=page.locator('(//li/a[@href="https://www.tranktechnologies.com/stock-trading-development-in-massachusetts"])[1]')
        self.p4=page.locator('(//li/a[@href="https://www.tranktechnologies.com/algo-trading-app-development-company"])[1]')
        self.p5=page.locator('(//li/a[@href="https://www.tranktechnologies.com/custom-trading-software-development-company"])[1]')
        self.p6=page.locator('(//li/a[@href="https://www.tranktechnologies.com/webportal-trading-development"])[1]')
        

        self.trading_option_list=[self.p0,self.p1,self.p2,self.p3,self.p4,self.p5,self.p6]


        #####health care
        self.p7=page.locator('(//li/a[@href="https://www.tranktechnologies.com/diet-and-nutrition-app-developement"])[1]')
        self.p8=page.locator('(//li/a[@href="https://www.tranktechnologies.com/health-tracking-app"])[1]')

        self.healthcare_option_list=[self.p7,self.p8]


        ##Fintech
        self.p9=page.locator('(//li/a[@href="https://www.tranktechnologies.com/pos-software-development-company"])[1]')
        self.p09=page.locator('(//li/a[@href="https://www.tranktechnologies.com/cryptocurrency-mobile-app-development-company"])[1]')

        self.Fintech_option_list=[self.p9,self.p09]


        ###custom
        self.p10=page.locator('(//li/a[@href="https://www.tranktechnologies.com/desktop-application-development-company"])[1]')
        self.p11=page.locator('(//li/a[@href="https://www.tranktechnologies.com/hrm-application-development-company"])[1]')
        self.p12=page.locator('(//li/a[@href="https://www.tranktechnologies.com/travel-mobile-app-development-company"])[1]')
        self.p13=page.locator('(//li/a[@href="https://www.tranktechnologies.com/dating-app-development-company"])[1]')
        self.p14=page.locator('(//li/a[@href="https://www.tranktechnologies.com/usa/custom-crm-development-company-usa"])[1]')
        self.p15=page.locator('(//li/a[@href="https://www.tranktechnologies.com/custom-crm-development-company"])[1]')
        self.p16=page.locator('(//li/a[@href="https://www.tranktechnologies.com/erp-app-development-company"])[1]')
        self.p17=page.locator('(//li/a[@href="https://www.tranktechnologies.com/e-learning-mobile-app-development-company"])[1]')
        self.p18=page.locator('(//li/a[@href="https://www.tranktechnologies.com/real-estate-mobile-app-development-company"])[1]')

        self.customer_option_list =[self.p10,self.p11,self.p12,self.p13,self.p14,self.p15,self.p16,self.p17,self.p18]


        
        ###RetailEcommerce
        self.p19=page.locator('(//li/a[@href="https://www.tranktechnologies.com/ecommerce-web-development-company"])[1]')
        self.p20=page.locator('(//li/a[@href="https://www.tranktechnologies.com/ecommerce-app-development"])[1]')


        self.Retail_Ecommerce_option_list=[self.p19,self.p20]

     ##########################################  

    def trading_options_clicking(self):
        for i in self.trading_option_list:
            self.verticals.hover()
            self.trading.hover()
            ##self.page.wait_for_timeout(5000)
            i.click()
            self.page.wait_for_load_state("load")
            self.page.go_back()


    def Healthcare_options_clicking(self):
            for i in self.healthcare_option_list:
                self.verticals.hover()
                self.Healthcare.hover()
                ##page.wait_for_timeout(5000)
                i.click()
                self.page.wait_for_load_state("load")
                self.page.go_back()


    def Fintech_options_clicking(self):
            for i in self.Fintech_option_list:
                self.verticals.hover()
                self.Fintech.hover()
                ##page.wait_for_timeout(5000)
                i.click()
                self.page.wait_for_load_state("load")
                self.page.go_back()


    def customApp_options_clicking(self):
            for i in  self.customer_option_list:
                self.verticals.hover()
                self.customApp.hover()
                ##page.wait_for_timeout(5000)
                i.click()
                self.page.wait_for_load_state("load")
                self.page.go_back()


    def Retail_Ecommerce_options_clicking(self):
            for i in self.Retail_Ecommerce_option_list:
                self.verticals.hover()
                self.Retail_Ecommerce.hover()
                ##page.wait_for_timeout(5000)
                i.click()
                self.page.wait_for_load_state("load")
                self.page.go_back()
