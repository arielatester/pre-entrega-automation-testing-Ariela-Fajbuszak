from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from .helpers import wait_for

class LoginPage:
    USERNAME = (By.ID, "user-name")
    PASSWORD = (By.ID, "password")
    BTN_LOGIN = (By.ID, "login-button")

    def __init__(self, driver):
        self.driver = driver

    def login(self, username, password):
        wait_for(self.driver, EC.visibility_of_element_located(self.USERNAME))
        self.driver.find_element(*self.USERNAME).send_keys(username)
        self.driver.find_element(*self.PASSWORD).send_keys(password)
        self.driver.find_element(*self.BTN_LOGIN).click()

class InventoryPage:
    TITLE = (By.CLASS_NAME, "title")
    INVENTORY_ITEM = (By.CLASS_NAME, "inventory_item")
    FIRST_ADD_BTN = (By.XPATH, "(//button[contains(@id,'add-to-cart')])[1]")
    CART_BADGE = (By.CLASS_NAME, "shopping_cart_badge")
    CART_LINK = (By.CLASS_NAME, "shopping_cart_link")

    def __init__(self, driver):
        self.driver = driver

    def validate_title(self):
        title = wait_for(self.driver, EC.visibility_of_element_located(self.TITLE)).text
        return title

    def has_products(self):
        return len(self.driver.find_elements(*self.INVENTORY_ITEM)) > 0

    def add_first_product(self):
        wait_for(self.driver, EC.element_to_be_clickable(self.FIRST_ADD_BTN)).click()

    def cart_count(self):
        badges = self.driver.find_elements(*self.CART_BADGE)
        return badges[0].text if badges else "0"

    def go_to_cart(self):
        self.driver.find_element(*self.CART_LINK).click()

class CartPage:
    ITEM_NAME = (By.CLASS_NAME, "inventory_item_name")

    def __init__(self, driver):
        self.driver = driver

    def get_first_item_name(self):
        return wait_for(self.driver, EC.visibility_of_element_located(self.ITEM_NAME)).text
