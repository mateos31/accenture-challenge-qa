import time
from behave import given, when, then
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

    driver.find_element(By.ID, "firstName").send_keys("Edward")
    driver.find_element(By.ID, "lastName").send_keys("Elric")

    driver.find_element(By.ID, "userEmail").send_keys("edward_elric@email.com")

    driver.find_element(By.XPATH, "//label[text()='Male']").click()

    driver.find_element(By.ID, "userNumber").send_keys("1100000000")

    driver.find_element(By.ID, "dateOfBirthInput").click()

    driver.find_element(By.CLASS_NAME, "react-datepicker__year-select").send_keys("1999")

    driver.find_element(By.CLASS_NAME, "react-datepicker__month-select").send_keys("September")

    driver.find_element(By.XPATH, "//div[text()='21']").click()

    subjects = driver.find_element(By.ID, "subjectsInput")
    subjects.send_keys("Computer")
    subjects.send_keys("\n")

    driver.find_element(By.XPATH, "//label[text()='Sports']").click()

    # Upload arquivo
    """
    file_path = os.path.abspath("arquivo.txt")
    with open("arquivo.txt", "w") as f:
        f.write("Arquivo de teste - Edward Elric")
    driver.find_element(By.ID, "uploadPicture").send_keys(file_path)
    """

    driver.find_element(By.ID, "currentAddress").send_keys("Sao Paulo SP")
    time.sleep(3)

    driver.execute_script("window.scrollBy(0, 500);")

    state_dropdown = driver.find_element(By.ID, "state")
    state_dropdown.click()

    state_option = driver.find_element(By.XPATH, "//div[text()='NCR']")
    state_option.click()

    city_dropdown = driver.find_element(By.ID, "city")
    city_dropdown.click()

    city_option = driver.find_element(By.XPATH, "//div[text()='Delhi']")
    city_option.click()


@then('ele clica para enviar o formuláro')
def step_impl(context):
    driver = context.driver
    submit_btn = driver.find_element(By.ID, "submit")
    submit_btn.click()
    time.sleep(5)


@given('que o usuário submeteu o formulário')
def step_impl(context):
    wait = WebDriverWait(context.driver, 10)
    modal_title = wait.until(
        EC.visibility_of_element_located((By.ID, "example-modal-sizes-title-lg"))
    )

    assert modal_title.text == "Thanks for submitting the form"


@when('visualizar o pop-up com os dados preenchidos')
def step_impl(context):
    wait = WebDriverWait(context.driver, 10)

    modal = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "modal-content")))

    rows = modal.find_elements(By.XPATH, "//table/tbody/tr")

    dados_modal = {}

    for row in rows:
        key = row.find_element(By.TAG_NAME, "td").text
        value = row.find_elements(By.TAG_NAME, "td")[1].text
        dados_modal[key] = value

    assert dados_modal["Student Name"] == "Edward Elric"
    assert dados_modal["Student Email"] == "edward_elric@email.com"
    assert dados_modal["Gender"] == "Male"
    assert dados_modal["Mobile"] == "1100000000"
    assert dados_modal["Date of Birth"] == "21 September,1999"
    assert dados_modal["Subjects"] == "Computer Science"
    assert dados_modal["Hobbies"] == "Sports"
    assert dados_modal["Address"] == "Sao Paulo SP"
    assert dados_modal["State and City"] == "NCR Delhi"


@then('deverá fechar o pop-up e o navegador')
def step_impl(context):
    wait = WebDriverWait(context.driver, 10)
    close_btn = wait.until(
        EC.visibility_of_element_located((By.ID, "example-modal-sizes-title-lg"))
    )
    close_btn.click()
