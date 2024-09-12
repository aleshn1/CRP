
# [CRP] The project is coded using a simple and intuitive structure presented below:

```bash
  crp  
   |
   |-- crp/                               # Implements app configuration
   |    |-- settings.py                    # Defines Global Settings
   |    |-- wsgi.py                        # Start the app in production
   |    |-- urls.py                        # Define URLs served by all apps/nodes
   |
   |-- apps/
   |    |
   |    |-- home/                          # A simple app that serve HTML files
   |    |    |-- views.py                  # Serve HTML pages for authenticated users
   |    |    |-- urls.py                   # Define some super simple routes  
   |    |
   |    |-- authentication/                # Handles auth routes (login and register)
   |    |    |-- urls.py                   # Define authentication routes  
   |    |    |-- views.py                  # Handles login and registration  
   |    |    |-- forms.py                  # Define auth forms (login and register) 
   |    |
   |    |-- static/
   |    |    |-- <css, JS, images>         # CSS files, Javascripts files
   |    |
   |    |-- templates/                     # Templates used to render pages
   |         |-- includes/                 # HTML chunks and components
   |         |    |-- navigation.html      # Top menu component
   |         |    |-- sidebar.html         # Sidebar component
   |         |    |-- footer.html          # App Footer
   |         |    |-- scripts.html         # Scripts common to all pages
   |         |
   |         |-- layouts/                   # Master pages
   |         |    |-- base-fullscreen.html  # Used by Authentication pages
   |         |    |-- base.html             # Used by common pages
   |         |
   |         |-- registration/                  # Authentication pages
   |         |    |-- login.html            # Login page
   |         |    |-- register.html         # Register page
   |         |
   |         |-- home/                      # UI Kit Pages
   |              |-- index.html            # Index page
   |              |-- 404-page.html         # 404 page
   |              |-- *.html                # All other pages
   |
   |-- requirements.txt                     # Development modules - SQLite storage
   |-- manage.py      
   |-- 
   
   ************************************************************************
```

Configuração do projeto:



criar venv
```
python -m venv <nome da venv>
```

```
<comando_de_instalação>
```

https://github.com/thiagopena/djangoSIGE
https://github.com/AlannKPerini/TUTORIAL_PROJETO_DJANGO_2024


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




