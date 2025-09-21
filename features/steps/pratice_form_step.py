import time
from behave import given, when, then
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@given('que o usuário acessa o site "{url}"')
def step_impl(context, url):
    context.driver.get(url)


@when('ele seleciona a opção "Forms" na página inicial')
def step_impl(context):
    wait = WebDriverWait(context.driver, 10)
    forms_btn = wait.until(EC.element_to_be_clickable((By.XPATH, "//h5[text()='Forms']")))
    forms_btn.click()

@then('ele acessa o formulário')
def step_impl(context):
    practice_form = WebDriverWait(context.driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//span[text()='Practice Form']"))
    )
    practice_form.click()


@given('que o usuário está com o formulário aberto')
def step_impl(context):
    assert "automation-practice-form" in context.driver.current_url

@when('ele preencher os dados do formulário AND enviar o arquivo txt')
def step_impl(context):
    driver = context.driver
    time.sleep(2)

    # Preencher nome e sobrenome
    driver.find_element(By.ID, "firstName").send_keys("Edward")
    driver.find_element(By.ID, "lastName").send_keys("Elric")
    time.sleep(2)

    #Preencher email
    driver.find_element(By.ID, "userEmail").send_keys("edward_elric@email.com")

    # Gênero
    driver.find_element(By.XPATH, "//label[text()='Male']").click()
    time.sleep(2)

    # Mobile
    driver.find_element(By.ID, "userNumber").send_keys("1100000000")
    time.sleep(2)

    # Date of Birth
    driver.find_element(By.ID, "dateOfBirthInput").click()
    time.sleep(2)
    driver.find_element(By.CLASS_NAME, "react-datepicker__year-select").send_keys("1999")
    time.sleep(2)
    driver.find_element(By.CLASS_NAME, "react-datepicker__month-select").send_keys("September")
    time.sleep(2)
    driver.find_element(By.XPATH, "//div[text()='21']").click()
    time.sleep(2)

    # Subjects
    subjects = driver.find_element(By.ID, "subjectsInput")
    subjects.send_keys("alchemist" + Keys.ENTER)
    #subjects.send_keys("\n")

    # Hobbies
    driver.find_element(By.ID, "hobbies-checkbox-1").click()

    # Upload arquivo
    """
    file_path = os.path.abspath("arquivo.txt")
    with open("arquivo.txt", "w") as f:
        f.write("Arquivo de teste - Edward Elric")
    driver.find_element(By.ID, "uploadPicture").send_keys(file_path)
    """

    # Endereço
    driver.find_element(By.ID, "currentAddress").send_keys("Sao Paulo SP")

@then('ele clica para enviar o formuláro')
def step_impl(context):
    driver = context.driver
    submit_btn = driver.find_element(By.ID, "submit")
    driver.execute_script("arguments[0].click();", submit_btn)
