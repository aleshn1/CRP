
Configuração do projeto:

criar venv
```
python -m venv <nome da venv>
```

```
<comando_de_instalação>
```

Especificações

Python
django
html5
css
Js
SQLITE3


# Arquivos de configuração da aplicação

O projeto vem com alguns arquivos de configuração pré-configurados, como:

- `settings.py:` Arquivo de configuração do Django.
- `manage.py`: é o arquivo que você usa para executar comandos do **Django**.
- `urls.py:` Arquivo de configuração das rotas do Django.
- `.gitignore:` Arquivo de configuração do Git, para ignorar arquivos e diretórios.
-  `db.sqlite3`: é o arquivo de banco de dados do projeto.
-  O arquivo `__init__.py` é um arquivo que indica que a pasta é um pacote Python. Ele vai aparecer em todas as pastas que contêm código Python. Muitas vezes, ele é um arquivo vazio.
  
Posteriormente, iremos modificar esses arquivos, bem como incluir alguns arquivos novos.

  Vamos abrir cada um desses arquivos e verificar para que eles servem.

Abra o arquivo **`settings.py:`** para alteração do idioma  e o horário padrão do Django. Faça a alteração conforme o exemplo abaixo:

```shell
LANGUAGE_CODE = 'pt-br'

TIME_ZONE = 'America/Sao_Paulo'

USE_I18N = True

USE_TZ = True
```
# 1° passo

criar venv 
python -m venv <nome da venv>

Windows
.\<nome_venv>\Scripts\activate

Linux
./source/bin/activate

# 2° passo

instalar dependencias 

pip install -r requirements.txt

3° passo

Criar o usuario(admin)

python manage.py createsuperuser

4° passo

Iniciar app

python manage.py runserver




