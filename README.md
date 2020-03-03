# api-python-flask-example
Template para criação de API com Python e Flask.

# introdução
API com serviços para administração de solicitações de "Fichas Catalográficas". No template, foram implementados 4 serviços para: listar todas as fichas, listar fichar por unidade, buscar ficha por id e alterar status de uma ficha.

# arquitetura
1. Python >= 3.7
2. Flask >= 1.1.1

# instalação
**1. Instalar o virtualenv para começar o projeto** 
* $ pip install virtualenv

**2. Ir para o diretório do projeto**

**3. Incluir as dependências do Flask**
* $ virtualenv .venv

**4. Ativar o virtualenv**

 No Linux
 * $ source .venv/bin/activate

 No Windows
 * Executar o arquivo .venv\Scripts\activate.bat

**5. Instalar o Flask**
 * $ pip install flask

**6. Criar um arquivo chamado "requirements.txt" com o conteúdo abaixo:**
 * flask==1.1.1

**7. Basta executar o rodar o arquivo "app.py" e consumir os serviços da api:**
 * $ python app.py

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

* **Example**

/fichas/1

* **Success Response:**

  * **Code:** 200 <br />
    **Content:** `{ id : 1, status : "Solicitado", solicitante: ... }`
                
* **Error Response:**

  * **Code:** 404 NOT FOUND <br />
    **Content:** `{'error': 'not found'}`
    
 **Mostrar todas as Fichas**
----
  Retorna json com dados de todas as fichas.

* **URL**

  /fichas/

* **Method:**

  `GET`
  
* **Example**

/fichas/

* **Success Response:**

  * **Code:** 200 <br />
    **Content:** `{ id : 1, status : "Solicitado", solicitante: ... }`
                
* **Error Response:**

  * **Code:** 404 NOT FOUND <br />
    **Content:** `{'error': 'not found'}`

 **Mostrar as Fichas de uma determinada unidade (descrição da unidade)**
----
  Retorna json com dados das fichas de uma unidade.

* **URL**

  /fichas/:unidade

* **Method:**

  `GET`
  
*  **URL Params**

   **Required:**
 
   `solicitante.unidade.descricao=[string]`

* **Example**

/fichas/Centro%20de%20Educação

* **Success Response:**

  * **Code:** 200 <br />
    **Content:** `{ id : 1, status : "Solicitado", solicitante: ... }`
                
* **Error Response:**

  * **Code:** 404 NOT FOUND <br />
    **Content:** `{'error': 'not found'}`

 **Inserir uma Ficha**
----
  Insere uma ficha catalográfica.

* **URL**

  /fichas/:unidade

* **Method:**

  `POST`
  
*  **URL Params**

   **Required:**
 
   Todos os campos

* **Example**

/fichas/Centro%20de%20Educação

* **Success Response:**

  * **Code:** 200 <br />
    **Content:** `{ id : 1, status : "Solicitado", solicitante: ... }`
                
* **Error Response:**

  * **Code:** 404 NOT FOUND <br />
    **Content:** `{'error': 'not found'}`
