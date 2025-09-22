from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@given('que o usuário acessa a aba "Alerts, Frame & Windows" do site "{url}"')
def step_impl(context, url):
    context.driver.get(url)
    wait = WebDriverWait(context.driver, 10)
    alerts_menu = wait.until(EC.element_to_be_clickable((By.XPATH, "//h5[text()='Alerts, Frame & Windows']")))
    alerts_menu.click()

@when('ele seleciona a opção "Browser Windows" AND clica no botão "New Window"')
def step_impl(context):
    wait = WebDriverWait(context.driver, 10)

    browser_windows = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Browser Windows']")))
    browser_windows.click()

    new_window_btn = wait.until(EC.element_to_be_clickable((By.ID, "windowButton")))
    new_window_btn.click()

@then('uma nova janela deve ser aberta com a mensagem "This is a sample page"')
def step_impl(context):
    driver = context.driver
    wait = WebDriverWait(driver, 10)

    original_window = driver.current_window_handle

    wait.until(EC.number_of_windows_to_be(2))

    for handle in driver.window_handles:
        if handle != original_window:
            driver.switch_to.window(handle)
            break

    message = wait.until(EC.visibility_of_element_located((By.ID, "sampleHeading")))
    assert message.text == "This is a sample page"

    driver.close()
    driver.switch_to.window(original_window)