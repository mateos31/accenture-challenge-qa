from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

@given('que o usuário acessa o site via "{url}"')
def step_impl(context, url):
    context.driver.get(url)
    context.wait = WebDriverWait(context.driver, 15)

@when('ele seleciona a opção "Widgets" na página inicial')
def step_impl(context):
    widgets = context.wait.until(EC.element_to_be_clickable((By.XPATH, f"//h5[text()='Widgets']")))
    widgets.click()
    context.driver.execute_script("window.scrollBy(0, 800);")

@when('ele clica no submenu "Progress Bar"')
def step_impl(context):
    progress_bar = context.wait.until(EC.element_to_be_clickable((By.XPATH, f"//span[text()='Progress Bar']")))
    progress_bar.click()

@when('ele inicia a progress bar')
def step_impl(context):
    context.start_button = context.wait.until(EC.element_to_be_clickable((By.ID, "startStopButton")))
    context.start_button.click()

@then('ele para a barra aos 25 por cento')
def step_impl(context):
    while True:
        progress_value = context.driver.find_element(By.CSS_SELECTOR, "div[role='progressbar']").get_attribute("aria-valuenow")
        context.progress_value = int(progress_value)
        if context.progress_value == 25:
            context.start_button.click()
            break
        time.sleep(0.1)
    time.sleep(5)

@then('valida que o valor é igual a 25')
def step_impl(context):
    assert context.progress_value <= 25, f"Erro: Progress bar passou de 25%! Valor atual: {context.progress_value}"

@when('ele inicia novamente até 100 por cento')
def step_impl(context):
    context.start_button.click()
    while True:
        progress_value = context.driver.find_element(By.CSS_SELECTOR, "div[role='progressbar']").get_attribute("aria-valuenow")
        context.progress_value = int(progress_value)
        if context.progress_value == 100:
            break
        time.sleep(0.08)
    time.sleep(5)

@then('ele reseta a progress bar')
def step_impl(context):
    reset_button = context.wait.until(EC.element_to_be_clickable((By.ID, "resetButton")))
    reset_button.click()
