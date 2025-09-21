Feature: Manipulação de tabelas

  Scenario: Usuário acessa a tabela de registros
    Given que o usuário acessa a opção "Elements" do site "https://demoqa.com/"
    When ele seleciona no submenu a opção "Web Tables"
    Then deverá visualizar a tabela de registro

  Scenario Outline: Usuário manipula registros na tabela
    Given que o usuário está na tabela de registro
    When ele clica em "Add" AND preenche os dados do funcionário com <Primeiro Nome>, <Último Nome>, <Email>, <Idade>, <Salário>, <Departamento> AND clica em "Submit"
    Then deverá ver o novo registro na tabela
    When ele edita o registro com <Novo Email>
    Then o registro deverá ser atualizado com sucesso
    When ele clica no botão para apagar o registro
    Then o registro deverá ser removido da tabela

    Examples:
      | Primeiro Nome | Último Nome | Email | Idade | Salário | Departamento | Novo Email |
      | John | Doe | john.doe@mail.com | 30 | 50000 | IT | john.doe_editado@mail.com |
      | Jane | Smith | jane.smith@mail.com | 25 | 60000 | HR | jane.smith_editado@mail.com |
      | Peter | Jones | peter.jones@mail.com | 45 | 75000 | Marketing | peter.jones_editado@mail.com |
      | Maria | Garcia | maria.garcia@mail.com | 35 | 55000 | Financeiro | maria.garcia_editado@mail.com |
      | Luiz | Santos | luiz.santos@mail.com | 28 | 48000 | Vendas | luiz.santos_editado@mail.com |
      | Fernanda | Lima | fernanda.lima@mail.com | 40 | 80000 | IT | fernanda.lima_editado@mail.com |
      | João | Pereira | joao.pereira@mail.com | 22 | 40000 | RH | joao.pereira_editado@mail.com |
      | Ana | Souza | ana.souza@mail.com | 50 | 90000 | Gestão | ana.souza_editado@mail.com |
      | Carlos | Oliveira | carlos.oliveira@mail.com | 33 | 62000 | Marketing | carlos.oliveira_editado@mail.com |
      | Patricia | Costa | patricia.costa@mail.com | 29 | 53000 | Financeiro | patricia.costa_editado@mail.com |
      | Ricardo | Dantas | ricardo.dantas@mail.com | 41 | 70000 | Vendas | ricardo.dantas_editado@mail.com |
      | Bruna | Martins | bruna.martins@mail.com | 26 | 58000 | RH | bruna.martins_editado@mail.com |