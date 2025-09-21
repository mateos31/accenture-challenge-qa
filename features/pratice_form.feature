Feature: Preenchimento do formulário

  Scenario: Usuário acesa o formulario
    Given que o usuário acessa o site "https://demoqa.com/"
    When ele seleciona a opção "Forms" na página inicial
    Then ele acessa o formulário

  Scenario: Usuário preenche e envia o Practice Form com sucesso
    Given que o usuário está com o formulário aberto
    When ele preencher os dados do formulário AND enviar o arquivo txt
    Then ele clica para enviar o formuláro

  Scenario:
    Given que o usuário submeteu o formulário
    When visualizar o pop-up com os dados preenchidos
    Then deverá fechar o pop-up e o navegador