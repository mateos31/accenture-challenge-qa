from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


@given('que o usuário acessa a opção "Interactions" do site "https://demoqa.com/" e selecionar a opção "Sortable" no submenu')
def step_impl(context):
    context.driver.get("https://demoqa.com/")
    wait = WebDriverWait(context.driver, 10)

    interactions = wait.until(EC.element_to_be_clickable((By.XPATH, "//h5[text()='Interactions']")))
    interactions.click()

    sortable = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Sortable']")))
    sortable.click()


@when('ele clica e arrasta nos itens da lista')
def step_impl(context):
    wait = WebDriverWait(context.driver, 10)
    context.driver.execute_script("window.scrollBy(0, 800);")

    items = wait.until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, "div.vertical-list-container div.list-group-item"))
    )

    time.sleep(2)

    context.original_order = [item.text for item in items]

    actions = ActionChains(context.driver)

    for i in range(len(items) - 1, 0, -1):
        source = items[0]
        target = items[i]  # último item
        actions.click_and_hold(source).move_to_element(target).release().perform()
        time.sleep(2)

        # Atualiza lista a cada iteração
        items = context.driver.find_elements(By.CSS_SELECTOR, "div.vertical-list-container div.list-group-item")

    # Nova ordem
    context.new_order = [item.text for item in items]

@then('ele reorganiza a lsita')
def step_impl(context):
    # Ordem esperada (decrescente)
    expected_order = context.original_order
    expected_order.reverse()

    assert context.new_order == expected_order, (
        f"Esperado: {expected_order}, mas obteve: {context.new_order}"
    )