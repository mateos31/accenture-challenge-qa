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

  Scenario Outline: Usuário manipula múltiplos registros na tabela
    Given que o usuário ainda está na tabela de registro
    When ele clica em "Add" AND preenche os dados do funcionário com "<Primeiro Nome>", "<Último Nome>", "<Email>", "<Idade>", "<Salário>", "<Departamento>" e clica em "Submit"
    Then deverá ver e apagar o registro na tabela equivalente ao "<Email>"

    Examples:
      | Primeiro Nome | Último Nome | Email                           | Idade | Salário | Departamento         |
      | Naruto        | Uzumaki     | naruto.uzumaki@konoha.com       | 17    | 15000   | Hokage               |
      | Obi-Wan       | Kenobi      | obiwan.kenobi@jedi.org          | 57    | 90000   | Jedi Council         |
      | Harry         | Potter      | harry.potter@hogwarts.uk        | 21    | 35000   | Ministry of Magic    |
      | Aragorn       | Elessar     | aragorn.elessar@gondor.gov      | 87    | 100000  | King's Court         |
      | Katniss       | Everdeen    | katniss.everdeen@district12.gov | 18    | 20000   | Rebellion            |
      | Tony          | Stark       | tony.stark@avengers.com         | 48    | 999999  | R&D                  |
      | Leia          | Organa      | leia.organa@rebellion.com       | 25    | 75000   | Alliance             |
      | Geralt        | of Rivia    | geralt.rivia@witcher.net        | 100   | 50000   | Witcher              |
      | Hermione      | Granger     | hermione.granger@hogwarts.uk    | 21    | 40000   | Ministry of Magic    |
      | Indiana       | Jones       | indiana.jones@adventurer.edu    | 50    | 70000   | Archaeology          |
      | Walter        | White       | walter.white@school.edu         | 52    | 85000   | Chemistry            |
      | Sherlock      | Holmes      | sherlock.holmes@221b.co.uk      | 35    | 65000   | Consulting Detective |