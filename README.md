# Auto_shop_postgres
Install dependencies:

'''
pip install -r requirements.txt
'''

Run docker process with postgres image:

'''
docker run -p 5432:5432 -e POSTGRES_PASSWORD=password postgres
'''

Run Django webserver 

'''
python manage.py runserver
'''
