 Feature: Barra de progresso

  Scenario: Usuário acessa a barra de progresso
    Given que o usuário acessa a opção "Widgets" do site "https://demoqa.com/" e selecionar a opção "Progessbar" no submenu
    When ele clica no botão "Start"
    Then deverá visualizar a progressão da barra
    When visualizar a barra em 25% AND clicar no botão "Pause"
    Then deverá visualizar a progressão da barra parar em 25%
    When clicar em "Start"
    Then deverá finalizar a progressão da barra em 100%