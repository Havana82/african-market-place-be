# african-market-place-be
Summary
This is tha API for ther afab-african-market user interface. This Api enables users to retrieve all product data, retrieve by categories,
and search for products by product name.

- Dependencie
- asgiref==3.7.2
- Django==4.2.3
- django-cors-headers
- django-environ
- djangorestframework
- gunicorn
- packaging
- Pillow
- python-dotenv
- pytz
- sqlparse
- tzdata
- CORS

## Set Up Instructions and Features
- Clone this repo 
- Create a virtual enivironment inside the repo folder
- Activate virtual environment
- install dependencies by running  pip install -r requirements.txt
- start app by running  python manage.py runserver
- app will run on http://127.0.0.1:8000/
- product data can be viewed on http://127.0.0.1:8000/api/products/
- Category data can be viewed on http://127.0.0.1:8000/api/category/
- Product can be viewed based on category on http://127.0.0.1:8000/api/categoryBasedProducts
-Each Category can be viewed by id on http://127.0.0.1:8000/api/category/id

