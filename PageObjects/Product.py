import idna.compat
from selenium.webdriver.common.by import By


class Product:
    product1 = "//div[contains(text(),'Sauce Labs Backpack')]"
    product2 = "//div[contains(text(),'Sauce Labs Bike Light')]"
    add_to_cart = "//button[@id='add-to-cart-sauce-labs-backpack']"
    add_to_cart1 = "//button[@id='add-to-cart-sauce-labs-bike-light']"
    Check_product_name1 = "//a[@id='item_4_title_link']"
    Check_product_name2 = "//a[@id='item_0_title_link']"
    Check_remove_button_of_product1 = "//button[@id='remove-sauce-labs-bike-light']"
    Check_remove_button_of_product2 = "//button[@id='remove-sauce-labs-backpack']"
    Click_Product_button = "//button[@id='add-to-cart-{}']"
        # "//div[contains(text(),'{}')]/parent::a/parent::div/following-sibling::div/div/following-sibling::button"
    # Click_Product_Button1 ="//div[contains(text(),'Sauce Labs Bike Light')]/parent::a/parent::div/following-sibling::div/div/following-sibling::button"
    Check_Remove_Button = "//button[@class='btn btn_secondary btn_small cart_button'][contains(text(),'Remove')]"
    Get_Cart_Products = "//div[@class='cart_list']//div[@class='inventory_item_name']"
    shopping_cart_container = "//a[@class='shopping_cart_link']"
    shpping_cart_count = "//span[@class='shopping_cart_badge']"
    Verify_Product= "//div[@class='inventory_item_name']"
    Continue_Shopping_Button = "//button[@name='continue-shopping']"
    HamBurger_Menu_Button="//div[@class='bm-burger-button']"
    Hambuger_Menu_Elements = "//nav[@class='bm-item-list']/a"
    Close_Hamurger_Menu ="//button[@id='react-burger-cross-btn']"
    Logout_button="//a[@id='logout_sidebar_link']"
    Product_lists="//*[@class='inventory_item_name']"
    Filter_Button= "//*[@class='product_sort_container']"
    Apply_Filter="//select[@class='product_sort_container']/option[{}]"

    def __init__(self, driver):
        self.driver = driver

    def add_product_click(self, productName):
        self.driver.find_element(By.XPATH, self.Click_Product_button.format(productName)).click()

    def verify_count(self, expectedCount):
        self.count = self.driver.find_element(By.XPATH, self.shpping_cart_count).text
        assert expectedCount ==int(self.count), "expected and actual count of product doesn't match"

    def shopping_cart(self):
        self.driver.find_element(By.XPATH, self.shopping_cart_container).click()

    def get_product_list_from_cart(self):
        CheckProducts = self.driver.find_elements(By.XPATH, self.Get_Cart_Products)
        Check=[i.text for i in CheckProducts]
        return Check
        # assert totalcount == int(self.count) ,"Invalid Count"

    def click_remove_button(self):
        buttons = self.driver.find_elements(By.XPATH, self.Check_Remove_Button)
        for button in buttons:
            button.click()

    def click_on_continue_shopping_button(self):
        self.driver.find_element(By.XPATH,self.Continue_Shopping_Button).click()


    def click_on_hamburger_menu(self):
        self.driver.find_element(By.XPATH, self.HamBurger_Menu_Button).click()

    def get_all_elements_of_hambeurger_menu(self):
        CheckElements =self.driver.find_elements(By.XPATH,self.Hambuger_Menu_Elements)
        Checkele = [i.text for i in CheckElements]
        return Checkele

    def click_on_close_button(self):
        self.driver.find_element(By.XPATH, self.Close_Hamurger_Menu).click()

    def collect_all_products_in_list(self):
        products_list=self.driver.find_elements(By.XPATH,self.Product_lists)
        products=[i.text for i in products_list]
        return products

    def click_on_filter(self):
        self.driver.find_element(By.XPATH,self.Filter_Button).click()

    def apply_filter(self,option):
        self.driver.find_element(By.XPATH,self.Apply_Filter.format(option)).click()

    def click_on_logout_button(self):
        self.driver.find_element(By.XPATH, self.Logout_button).click()




   # def verify_products(self):
    #    productslist= self.driver.find_element(By.XPATH, self.Verify_Products).text
    #    print(productslist)


        # check = self.driver.find_element(By.XPATH, self.Check_product_name1).text
        # assert expectedproducrname1 == check, "product doesn't match"
        # check1 = self.driver.find_element(By.XPATH, self.Check_product_name2).text
        # assert expectedproductname2 == check1, "product doesn't match"

    # def Click_Remove_button(self):
    # Checkname=self.driver.find_element(By.XPATH,self.Check_product_name1).text
    # assert Checkname == Expected_product_name1, "Invalid product"
    # self.driver.find_element(By.XPATH,self.Check_product_name1).click()
    # Checkname1=self.driver.find_element(By.XPATH,self.Check_product_name2).text
    # assert Checkname1 == Expected_product_name2, "Invalid product"
    # self.driver.find_element(By.XPATH,self.Check_product_name2).click()

     # def click_button(self):
        # self.driver.find_element(By.XPATH,self.Click_Product_button).click()
        # self.driver.find_element(By.XPATH,self.Click_Product_Button1).click()

    # def check_cart_count(self):
    #     # self.check_count= self.driver.find_element(By.XPATH, self.shpping_cart_count).text