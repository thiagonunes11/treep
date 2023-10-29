Claro, aqui está o texto com a alteração:

**Como abrir a aplicação**

Para abrir a aplicação, siga estas etapas:

1. **Certifique-se de ter o Python instalado**.
2. Faça o **git clone** da aplicação para o seu computador.
3. **Instale o Django** caso não tenha instalado. Para isso, execute o seguinte comando:

```
pip install django
```

4. **Instale o Pillow** caso não tenha instalado. Para isso, execute o seguinte comando:

```
pip install Pillow
```

5. **Inicie o ambiente virtual** com o comando:

```
python -m venv venv
```

6. **Ative o ambiente virtual** com o comando:

```
source venv/bin/activate
```

7. **Rode o comando** `python manage.py runserver` para iniciar o servidor da aplicação.

O servidor da aplicação irá gerar um endereço de IP para abrir a aplicação. Para visualizar o endereço de IP, execute o seguinte comando:

```
python manage.py runserver --host 0.0.0.0
```

O endereço de IP será exibido no console. Abra o navegador e navegue até o endereço de IP para abrir a aplicação.

**Exemplo**

Após seguir as etapas acima, o endereço de IP da aplicação será exibido no console da seguinte forma:

```
[2023-10-29 12:00:00,786] INFO: Starting development server at http://0.0.0.0:8000/
```

Abra o navegador e navegue até o endereço `http://0.0.00.0:8000/` para abrir a aplicação.

**Observações**

* Se você estiver usando o Windows, é necessário abrir o prompt de comando como administrador antes de iniciar o ambiente virtual.
* Se você estiver usando o macOS, é necessário abrir o terminal como administrador antes de iniciar o ambiente virtual.

Espero que isso ajude!