 Feature: Drag and drop

  Scenario: Usuário acessa alista ordenavel
    Given que o usuário acessa a opção "Interactions" do site "https://demoqa.com/" e selecionar a opção "Sortable" no submenu
    When ele clica e arrasta nos itens da lista
    Then ele reorganiza a lsita