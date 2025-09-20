Feature: Gerenciamento de usuário e livros na DemoQA

  Background:
    Given a base URL "https://demoqa.com"

  Scenario: Criar e autorizar usuário
    When eu faço uma requisição POST para "/Account/v1/User" com os dados do novo usuário
    Then o usuário deve ser criado com sucesso

    When eu faço uma requisição POST para "/Account/v1/GenerateToken" com as credenciais do usuário
    Then deve ser retornado um Access Token válido

    When eu faço uma requisição POST para "/Account/v1/Authorized"
    Then a resposta deve confirmar que o usuário está autorizado


  Scenario: Alugar livros para o usuário
    Given que o usuário já possui um Access Token válido
    When eu faço uma requisição GET para "/BookStore/v1/Books"
    Then devo visualizar a lista de livros disponíveis

    When eu faço uma requisição POST para "/BookStore/v1/Books" escolhendo dois livros
    Then os dois livros devem ser alugados para o usuário

    When eu faço uma requisição GET para "/Account/v1/User/" informando o ID no final da URL
    Then devo visualizar os detalhes do usuário com os livros alugados
