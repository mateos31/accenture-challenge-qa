 Feature: Abertura de nova janela

  Scenario: Usuário abre uma nova janela e valida a mensagem exibida
    Given que o usuário acessa a aba "Alerts, Frame & Windows" do site "https://demoqa.com/"
    When ele seleciona a opção "Browser Windows" AND clica no botão "New Window"
    Then uma nova janela deve ser aberta com a mensagem "This is a sample page"