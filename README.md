# api-python-flask-example
Template para criação de API com Python e Flask.

# introdução
API com serviços para administração de solicitações de "Fichas Catalográficas". No template, foram implementados 4 serviços para: listar todas as fichas, listar fichar por unidade, buscar ficha por id e alterar status de uma ficha.

# arquitetura
1. Python >= 3.7
2. Flask >= 1.1.1

# instalação
**1. Instalar o virtualenv para começar o projeto** 
$ pip install virtualenv

**2. Ir para o diretório do projeto**

**3. Incluir as dependências do Flask**
$ virtualenv .venv

**4. Ativar o virtualenv**

No Linux
$ source .venv/bin/activate

No Windows
Executar o arquivo .venv\Scripts\activate.bat

**5. Instalar o Flask**
$ pip install flask

**6. Criar um arquivo chamado "requirements.txt" com o conteúdo abaixo:**
flask==1.1.1

**7. Basta executar o rodar o arquivo "app.py" e consumir os serviços da api:**
$ python app.py

# documentação da api

**Mostrar Ficha**
----
  Retorna json com dados de uma ficha.

* **URL**

  /fichas/:id

* **Method:**

  `GET`
  
*  **URL Params**

   **Required:**
 
   `id=[integer]`

* **Data Params**

  None

* **Success Response:**

  * **Code:** 200 <br />
    **Content:** `{ id : 1, status : "Solicitado", solicitante: ... }`
                
* **Error Response:**

  * **Code:** 404 NOT FOUND <br />
    **Content:** `{'error': 'not found'}`

  OR

  * **Code:** 401 UNAUTHORIZED <br />
    **Content:** `{ error : "You are unauthorized to make this request." }`

* **Sample Call:**

  ```javascript
    $.ajax({
      url: "/fichas/1",
      dataType: "json",
      type : "GET",
      success : function(r) {
        console.log(r);
      }
    });
  ```
