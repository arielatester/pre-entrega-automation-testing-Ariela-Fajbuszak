from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

DEFAULT_TIMEOUT = 10

def wait_for(driver, condition, timeout=DEFAULT_TIMEOUT):
    # Espera explícita genérica
    return WebDriverWait(driver, timeout).until(condition)
