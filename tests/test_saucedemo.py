import pytest
from utils.pages import LoginPage, InventoryPage, CartPage
from selenium.webdriver.support import expected_conditions as EC
from utils.helpers import wait_for

USERNAME = "problem_user"
PASSWORD = "secret_sauce"
BASE_URL = "https://www.saucedemo.com/"

@pytest.mark.login
def test_login_ok(driver):
    driver.get(BASE_URL)
    login = LoginPage(driver)
    login.login(USERNAME, PASSWORD)
    wait_for(driver, EC.url_contains("/inventory.html"))
    assert "/inventory.html" in driver.current_url

@pytest.mark.inventory
#def test_inventory_validation(driver):
def test_inventario_validacion(driver):
    driver.get(BASE_URL)
    login = LoginPage(driver)
    login.login(USERNAME, PASSWORD)
    inventory = InventoryPage(driver)
    assert inventory.validate_title().lower() == "products"
    assert inventory.has_products(), "No hay productos"

@pytest.mark.cart
#def test_cart_add_and_verify(driver):
def test_agregar_carrito_y_verificar(driver):
    driver.get(BASE_URL)
    login = LoginPage(driver)
    login.login(USERNAME, PASSWORD)
    inventory = InventoryPage(driver)
    inventory.add_first_product()
    assert inventory.cart_count() == "1"
    inventory.go_to_cart()
    cart = CartPage(driver)
    item_name = cart.get_first_item_name()
    assert item_name != "", "El producto no aparece en el carrito"


