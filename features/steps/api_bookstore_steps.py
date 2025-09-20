import random

import requests
from behave import given, when, then


BASE_URL = "https://demoqa.com"
USER_DATA = {
    "userName": f"edward_elric3{random.randint(1,100)}",
    "password": "Fullmetal123!"
}


context_data = {
    "userID": None,
    "token": None
}


@given('a base URL "{url}"')
def step_impl(context, url):
    context.base_url = url
    assert url in BASE_URL


@when('eu faço uma requisição POST para "/Account/v1/User" com os dados do novo usuário')
def step_impl(context):
    response = requests.post(f"{BASE_URL}/Account/v1/User", json=USER_DATA)
    context.response = response
    if response.status_code == 201:
        context_data["userID"] = response.json().get("userID")


@then('o usuário deve ser criado com sucesso')
def step_impl(context):
    assert context.response.status_code == 201, f"Erro: {context.response.text}"


@when('eu faço uma requisição POST para "/Account/v1/GenerateToken" com as credenciais do usuário')
def step_impl(context):
    response = requests.post(f"{BASE_URL}/Account/v1/GenerateToken", json=USER_DATA)
    context.response = response
    if response.status_code == 200:
        context_data["token"] = response.json().get("token")


@then('deve ser retornado um Access Token válido')
def step_impl(context):
    assert context.response.status_code == 200
    assert "token" in context.response.json()


@when('eu faço uma requisição POST para "/Account/v1/Authorized"')
def step_impl(context):
    response = requests.post(f"{BASE_URL}/Account/v1/Authorized", json=USER_DATA)
    context.response = response


@then('a resposta deve confirmar que o usuário está autorizado')
def step_impl(context):
    assert context.response.status_code == 200
    assert context.response.json() is True


@given('que o usuário já possui um Access Token válido')
def step_impl(context):
    assert context_data["token"] is not None


@when('eu faço uma requisição GET para "/BookStore/v1/Books"')
def step_impl(context):
    response = requests.get(f"{BASE_URL}/BookStore/v1/Books",)
    context.response = response
    context.books = response.json().get("books")


@then('devo visualizar a lista de livros disponíveis')
def step_impl(context):
    assert context.response.status_code == 200
    assert len(context.books) > 0


@when('eu faço uma requisição POST para "/BookStore/v1/Books" escolhendo dois livros')
def step_impl(context):
    book_ids = [context.books[0]["isbn"], context.books[1]["isbn"]]

    payload = {
        "userId": context_data["userID"],
        "collectionOfIsbns": [{"isbn": book} for book in book_ids]
    }

    response = requests.post(f"{BASE_URL}/BookStore/v1/Books", json=payload)
    context.response = response
    context.chosen_books = book_ids


@then('os dois livros devem ser alugados para o usuário')
def step_impl(context):
    assert context.response.status_code in [200, 201], f"Erro: {context.response.text}"


@when('eu faço uma requisição GET para "/Account/v1/User/" informando o ID no final da URL')
def step_impl(context):
    response = requests.get(f"{BASE_URL}/Account/v1/User/{context_data['userID']}")
    context.response = response


@then('devo visualizar os detalhes do usuário com os livros alugados')
def step_impl(context):
    assert context.response.status_code == 200
    data = context.response.json()
    assert "books" in data
    assert len(data["books"]) >= 2
