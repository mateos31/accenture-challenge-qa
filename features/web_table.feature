Feature: Manipulação de tabelas

  Scenario: Usuário acessa a tabela de registros
    Given que o usuário acessa a opção "Elements" do site "https://demoqa.com/"
    When ele seleciona no submenu a opção "Web Tables"
    Then deverá visualizar a tabela de registro

  Scenario: Usuário manipula registros na tabela
    Given que o usuário está na tabela de registro
    When ele clica em "Add" AND preenche os dados do funcionário AND clica em "Submit"
    Then deverá ver o novo registro na tabela
    When ele edita o registro com email diferente
    Then o registro deverá ser atualizado com sucesso
    When ele clica no botão para apagar o registro
    Then o registro deverá ser removido da tabela