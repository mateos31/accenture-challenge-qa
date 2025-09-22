Feature: Barra de progresso

  Scenario: Usuário controla a barra de progresso
    Given que o usuário acessa o site via "https://demoqa.com/"
    When ele seleciona a opção "Widgets" na página inicial
    And ele clica no submenu "Progress Bar"
    And ele inicia a progress bar
    Then ele para a barra aos 25 por cento
    And valida que o valor é igual a 25
    When ele inicia novamente até 100 por cento
    Then ele reseta a progress bar