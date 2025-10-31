




class Inventory_page:


    URL CURRENT= "/inventory.html"

    def __init__(self, driver):
        self.driver = driver

    def is_at_page(self):
        return self.URL_CURRENT self.driver.current_url