class technology:
    def __init__(self, page): ####defining the constructor
        self.page=page
        ##vertical locator

        self.technologies=page.locator('(//li[@class="drop_down"])[2]') ####technologies hover()

    ####submenus of technologies
        self.ecommercedevelopment =page.locator('//li[@data-id="ecomm"]')
        self.mobileappdevelopment=page.locator('//li[@data-id="mobileApp"]')
        self.artificialIntelligence=page.locator('//li[@data-id="aipage"]')
        

        ###submenus ofecommercedevelopment
             
        self.p0=page.locator('(//a[@href="https://www.tranktechnologies.com/magento-development"])[1]')
        self.p1=page.locator('(//a[@href="https://www.tranktechnologies.com/codeigniter-development"])[1]')
        self.p2=page.locator('(//a[@href="https://www.tranktechnologies.com/big-commerce"])[1]')
        self.p3=page.locator('(//a[@href="https://www.tranktechnologies.com/cs-cart-development"])[1]')
        self.p4=page.locator('(//a[@href="https://www.tranktechnologies.com/nopcommerce-design-and-development-company"])[1]')
        self.p5=page.locator('(//a[@href="https://www.tranktechnologies.com/laravel-development"])[1]')
        self.p6=page.locator('(//a[@href="https://www.tranktechnologies.com/drupal-development"])[1]')
        self.p7=page.locator('(//a[@href="https://www.tranktechnologies.com/joomla-development"])[1]')
        self.p8=page.locator('(//a[@href="https://www.tranktechnologies.com/express-js-development"])[1]')
        self.p9=page.locator('(//a[@href="https://www.tranktechnologies.com/opencart-development"])[1]')
        self.p10=page.locator('(//a[@href="https://www.tranktechnologies.com/wordpress-development"])[1]')
        self.p11=page.locator('(//a[@href="https://www.tranktechnologies.com/shopify-development"])[1]')
        self.p12=page.locator('(//a[@href="https://www.tranktechnologies.com/node-js-development"])[1]')
        self.p13=page.locator('(//a[@href="https://www.tranktechnologies.com/prestashop-development"])[1]')
        self.p14=page.locator('(//a[@href="https://www.tranktechnologies.com/wix-development"])[1]')
        self.p15=page.locator('(//a[@href="https://www.tranktechnologies.com/react-js-development"])[1]')
        
        self.ecommerce_option_list=[self.p0,self.p1,self.p2,self.p3,self.p4,self.p5,self.p6,self.p7,self.p8,self.p9,self.p10,self.p11,self.p12,self.p13,self.p14,self.p15]


        ####submenu for mobile app
        self.p16=page.locator('(//a[@href="https://www.tranktechnologies.com/react-native-mobile-app-development"])[1]')
        self.p17=page.locator('(//a[@href="https://www.tranktechnologies.com/xamarin-mobile-app-development"])[1]')
        self.p18=page.locator('(//a[@href="https://www.tranktechnologies.com/flutter-mobile-app-development"])[1]')
        self.p19=page.locator('(//a[@href="https://www.tranktechnologies.com/swift-mobile-app-development"])[1]')
        self.p20=page.locator('(//a[@href="https://www.tranktechnologies.com/ionic-mobile-app-development"])[1]')
        self.p21=page.locator('(//a[@href="https://www.tranktechnologies.com/enterprise-mobile-app-development"])[1]')
        self.p22=page.locator('(//a[@href="https://www.tranktechnologies.com/kotlin-mobile-app-development"])[1]')
        self.p23=page.locator('(//a[@href="https://www.tranktechnologies.com/appointment-booking-development"])[1]')
    
    
        self.mobileappdevelopment_list=[self.p16,self.p17,self.p18,self.p19,self.p20,self.p21,self.p22,self.p23]

    ###Articificial inteligence
        self.artificialIntelligence_list=[]

    
    def ecommerce_options_click(self):

        for i in self.ecommerce_option_list:

        # Open Technologies menu
           self.technologies.hover()

        # Wait for Ecommerce submenu
           self.ecommercedevelopment.wait_for(state="visible")

        # Hover over Ecommerce Development
           self.ecommercedevelopment.hover()

        # Wait for the target link
           i.wait_for(state="visible")

        # Click the link
           i.click()

           self.page.wait_for_load_state("load")

        # Navigate back
           self.page.go_back(wait_until="load")


    def mobileappdevelopment_options_click(self):

        for i in self.mobileappdevelopment_list:

        # Open Technologies menu
           self.technologies.hover()

        # Wait for Mobile App Development submenu
           self.mobileappdevelopment.wait_for(state="visible")

        # Hover over Mobile App Development
           self.mobileappdevelopment.hover()

        # Wait for target link
           i.wait_for(state="visible")

        # Click the link
           i.click()

           self.page.wait_for_load_state("load")

        # Navigate back
           self.page.go_back(wait_until="load")


    def artificialIntelligence_options_click(self):

        for i in self.artificialIntelligence_list:

            self.technologies.hover()

            self.artificialIntelligence.wait_for(state="visible")

            self.artificialIntelligence.hover()

            i.wait_for(state="visible")
            i.click()

            self.page.wait_for_load_state("load")

            self.page.go_back(wait_until="load")
