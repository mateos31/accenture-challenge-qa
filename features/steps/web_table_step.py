import time

from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@given('que o usuário acessa a opção "Elements" do site "{url}"')
def step_impl(context, url):
    context.driver.get(url)
    wait = WebDriverWait(context.driver, 10)
    elements_menu = wait.until(EC.element_to_be_clickable((By.XPATH, "//h5[text()='Elements']")))
    elements_menu.click()

@when('ele seleciona no submenu a opção "Web Tables"')
def step_impl(context):
    wait = WebDriverWait(context.driver, 10)

    web_tables = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Web Tables']")))
    web_tables.click()

@then('deverá visualizar a tabela de registro')
def step_impl(context):
    table = WebDriverWait(context.driver, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "rt-table"))
    )
    assert table.is_displayed()
    time.sleep(2)

@given('que o usuário está na tabela de registro')
def step_impl(context):
    assert "webtables" in context.driver.current_url


@when('ele clica em "Add" AND preenche os dados do funcionário AND clica em "Submit"')
def step_impl(context):
    wait = WebDriverWait(context.driver, 10)
    context.driver.execute_script("window.scrollBy(0, 500);")
    time.sleep(3)

    # Clica no botão Add
    add_btn = wait.until(EC.element_to_be_clickable((By.ID, "addNewRecordButton")))
    add_btn.click()
    time.sleep(3)

    # Preenche os campos
    context.driver.find_element(By.ID, "firstName").send_keys("Edward")
    context.driver.find_element(By.ID, "lastName").send_keys("Elric")
    context.driver.find_element(By.ID, "userEmail").send_keys("edward.elric@email.com")
    context.driver.find_element(By.ID, "age").send_keys("17")
    context.driver.find_element(By.ID, "salary").send_keys("5000")
    context.driver.find_element(By.ID, "department").send_keys("alchemy")

    # Submete
    context.driver.find_element(By.ID, "submit").click()

    # Armazena o email para identificar o registro
    context.current_email = "edward.elric@email.com"


@then('deverá ver o novo registro na tabela')
def step_impl(context):
    wait = WebDriverWait(context.driver, 10)
    cell = wait.until(EC.visibility_of_element_located((By.XPATH, f"//div[@class='rt-td' and text()='{context.current_email}']")))
    assert cell.is_displayed()


@when('ele edita o registro com email diferente')
def step_impl(context):
    wait = WebDriverWait(context.driver, 10)

    # Clica no botão Edit correspondente ao registro
    edit_btn = wait.until(EC.element_to_be_clickable((
        By.XPATH, f"//div[text()='{context.current_email}']/following-sibling::div//span[@title='Edit']"
    )))
    edit_btn.click()

    # Limpa e altera o campo de email
    email_input = wait.until(EC.visibility_of_element_located((By.ID, "userEmail")))
    email_input.clear()
    email_input.send_keys("edward.elric2@email.com")

    # Submete
    context.driver.find_element(By.ID, "submit").click()

    # Atualiza o email atual
    context.current_email = "edward.elric2@email.com"


@then('o registro deverá ser atualizado com sucesso')
def step_impl(context):
    wait = WebDriverWait(context.driver, 10)
    cell = wait.until(EC.visibility_of_element_located((By.XPATH, f"//div[@class='rt-td' and text()='{context.current_email}']")))
    assert cell.text == context.current_email


@when('ele clica no botão para apagar o registro')
def step_impl(context):
    wait = WebDriverWait(context.driver, 10)

    delete_btn = wait.until(EC.element_to_be_clickable((
        By.XPATH, f"//div[text()='{context.current_email}']/following-sibling::div//span[@title='Delete']"
    )))
    delete_btn.click()


@then('o registro deverá ser removido da tabela')
def step_impl(context):
    # Garante que o registro não está mais na tabela
    cells = context.driver.find_elements(By.XPATH, f"//div[@class='rt-td' and text()='{context.current_email}']")
    assert len(cells) == 0