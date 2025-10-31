import os
import pytest
import logging
import time
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

# --- Configuración inicial de logs ---
os.makedirs("logs", exist_ok=True)
logging.basicConfig(
    filename="logs/execution.log",
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    encoding="utf-8"
)

# --- Fixture principal del driver ---
@pytest.fixture
def driver():
    """Inicializa el driver de Chrome, maximiza ventana y espera antes de cerrar."""
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    service = ChromeService(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    yield driver
    time.sleep(3)  # 🔹 Pausa visual antes de cerrar
    driver.quit()

# --- Fixture automático entre tests ---
@pytest.fixture(autouse=True)
def pausa_entre_tests():
    """Pausa automática de 3 segundos entre tests."""
    yield
    time.sleep(3)

# --- Hook: capturar screenshot si el test falla ---
@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    """Captura screenshot automáticamente en caso de fallo."""
    outcome = yield
    rep = outcome.get_result()
    if rep.when == "call" and rep.failed:
        driver = item.funcargs.get("driver", None)
        if driver:
            os.makedirs("reports", exist_ok=True)
            ts = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"reports/FAILED_{item.name}_{ts}.png"
            driver.save_screenshot(filename)
            logging.error(f"Screenshot guardado: {filename}")
