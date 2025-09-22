# Desafio de automação de testes

---

## Tecnologias utilizadas
Para este desafio, foram utilizadas as seguintes bibliotecas e ferramentas:

* **Python:** A linguagem de programação principal. A versão mais recente é recomendada.
* **Selenium:** Usado para a automação de testes de frontend, simulando interações do usuário com o navegador.
* **Requests:** Essencial para a realização de testes de API (backend), permitindo fazer requisições HTTP.
* **Behave:** Um *framework* de BDD (*Behavior-Driven Development*) que está substituindo o Cucumber. Ele permite escrever cenários de teste em linguagem natural usando a sintaxe Gherkin, tornando os testes mais legíveis e fáceis de entender.

---

## Como executar o projeto
Para rodar o projeto, siga os seguintes passos:

1.  Tenha o **Python** instalado em sua máquina.
2.  Instale as bibliotecas necessárias com o seguinte comando:
    ```bash
    pip install selenium behave requests
    ```

> Embora não seja obrigatório, o **PyCharm** é uma IDE (ambiente de desenvolvimento integrado) que pode facilitar o gerenciamento das bibliotecas e dependências do projeto.

---

## Executando os testes

Para executar os testes, utilize o comando `behave` no terminal:

```bash
behave
```

No entanto, a estrutura dos testes (organizada por features) permite a execução individual de cada uma delas, o que pode ser mais eficiente. Para isso, use o seguinte comando:
```bash
behave .\features\nome_da_feature.feature
```

## Desafios e observações

Durante a execução do projeto, encontrei alguns pontos que merecem destaque:

### Testes de backend
Não foi possível realizar algumas chamadas de API que exigiam autorização. As tentativas feitas tanto via código quanto diretamente no Swagger fornecido não funcionaram. Acredito que possa ser um problema temporário, mas não houve tempo hábil para investigar mais a fundo.

### Testes de frontend
* **Itens arrastáveis (*Sortable*):** O site já apresentava a lista de itens arrastáveis em ordem crescente. Para validar a funcionalidade de drag-and-drop, optei por inverter a ordem dos itens ao realizar o teste.
* **Formulário de prática (*Practice Form*):** Não foi possível realizar o *upload* de um arquivo. No entanto, o restante dos campos do formulário foi preenchido com sucesso.
