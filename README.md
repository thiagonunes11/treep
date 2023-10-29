**Como abrir a aplicação**

Para abrir a aplicação, siga estas etapas:

1. **Instale o Python**, caso não tenha instalado. Você pode seguir as instruções no site oficial do Python.

2. Faça o **git clone** da aplicação para o seu computador.

3. **Crie e ative um ambiente virtual** para isolar as dependências da aplicação. Você pode fazer isso com os seguintes comandos:

   ```
   python -m venv venv
   ```

   - No Windows:

     ```
     venv\Scripts\activate
     ```

   - No macOS ou Linux:

     ```
     source venv/bin/activate
     ```

4. **Instale as dependências do projeto** a partir do arquivo `requirements.txt`. Para fazer isso, execute o seguinte comando:

   ```
   pip install -r requirements.txt
   ```

5. **Inicie o servidor da aplicação** com o comando:

   ```
   python manage.py runserver
   ```

O servidor da aplicação irá gerar um endereço de IP para abrir a aplicação. Esse endereço de IP será exibido no console. Abra o navegador e acesse o endereço exibido no console para abrir a aplicação.

**Exemplo**

Após seguir as etapas acima, o endereço de IP da aplicação será exibido no console da seguinte forma:

```
[2023-10-29 12:00:00,786] INFO: Starting development server at http://127.0.0.1:8000/
```

Abra o navegador e acesse o endereço `http://127.0.0.1:8000/` para abrir a aplicação.

**Observações**

* Se você estiver usando o Windows, é necessário abrir o prompt de comando como administrador antes de iniciar o ambiente virtual.
* Se você estiver usando o macOS, é necessário abrir o terminal com permissões de administrador antes de iniciar o ambiente virtual.

Espero que isso ajude!