# LoCar-Rest
[![PyPI](https://img.shields.io/pypi/pyversions/Django.svg)]()
[![PyPI](https://img.shields.io/badge/django-2.1-green.svg)]()
[![PyPI](https://img.shields.io/badge/django%20REST%20framework-3.9-red.svg)]()
[![license](https://img.shields.io/badge/license-MIT-brightgreen.svg)]()

## Requirements
- Python
- Virtualenv
- Django
- Django REST Framework
- Django-filter
- Django-cors-headers
- Gunicorn
- Django-heroku
- Psycopg2-binary

## How to install
Step 1: Make the clone of this repository with the command ```git clone https://github.com/Kmiokande/LoCar-Rest.git```

Step 2: In the **LoCar-Rest/** directory, type the command ```virtualenv -p python3 'virtualenvname'```

Step 3: To activate the virtual environment enter the command ```source virtualenv/bin/activate```

Step 4: To install the dependencies use the command ```pip install -r requirements.txt```

Step 5: To do the **makemigrations** use the command ```python manage.py makemigrations```

Step 6: Migrate with the command ```python manage.py migrate```

Step 7: To start the server enter the command ```python manage.py runserver```


