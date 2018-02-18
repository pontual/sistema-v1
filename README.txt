Sistema

(C) 2018 Pontual Exportação e Importação Ltda., Heitor Chang

License: MIT

Developed with Django 2.0.1

The initial secret key has been replaced with 'xxxxx...' in settings.orig.py

Front-end: Bootstrap 4

There are no restrictions on duplicates.

In Pontual, sometimes the factory sent products with slight color differences, but with the same code.

See TODO.txt


Sistema Setup:

git clone https://github.com/pontual/sistema

cd sistema/sistema
cp settings.debug.py settings.py

cd ..
python manage.py migrate

python manage.py createsuperuser

Download fotos_640 from Google Drive

Edit registros/bulk_add_produtos.py "FOTOS_DIR"
Run bulk_add_produtos.py inside python manage shell

python manage.py shell
from registros.bulk_add_produtos import add_produtos
add_produtos()

Download clientes.csv from Gmail (it is not in repo)

Edit registros/bulk_add_clientes.py file location
Run bulk_add_clientes.py inside python manage shell
from registros.bulk_add_clientes import add_clientes
add_clientes()

python manage.py runserver

Log in to /admin with the superuser

Create a Configuracao in Registros with Pontual as the active company and create a currency

Navigate to /sistema to check that data was loaded correctly


Catalogo Setup:

python manage.py shell
from catalogo.import_produtos import import_all
import_all()
