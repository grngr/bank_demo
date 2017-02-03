# Prerequisites
## Install postgres
CREATE DATABASE poc_bank  
    WITH  
    OWNER = postgres  
    ENCODING = 'UTF8'  
    CONNECTION LIMIT = -1;  

COMMENT ON DATABASE poc_bank  
    IS 'sample db for proof of concept bank';  

## Install nginx
download pcre 1, openssl and nginx sources  
cd /path/to/downloaded/source/nginx-1.10.2  
./configure --prefix=/installation/location/nginx-1.10.2 --with-pcre=/path/to/downloaded/source/pcre-8.38 --with-http_ssl_module --with-openssl=/path/to/downloaded/source/openssl-1.1.0c  

## Install through pip
pip install django  
pip install psycopg2  
pip install gunicorn  
pip install djangorestframework  
pip install markdown  

## Create and activate virtual environment. Initiate the server
cd /path/to/project/directory
virtualenv -p `which python3` bank_demo

cd bank_demo  
source bin/activate  

cd poc_bank  
python manage.py makemigrations fund_transfer  
python manage.py migrate  

python manage.py createsuperuser  
admin / blank email / wordpass / wordpass  

(For test purpose only: python manage.py runserver)  
path/to/nginx-1.10.2/sbin/nginx  
gunicorn -b 127.0.0.1:8000 poc_bank.wsgi:application  

## To stop
Ctrl+C  
nginx -s stop  
deactivate  

# Application Login, Admin and REST URLS

## Application Login URL
http://localhost:8080  

## Admin URL
http://localhost:8080/admin  

## REST URL
http://localhost:8080/api/same_payee/  
http://localhost:8080/api/other_payee/  
http://localhost:8080/api/customer/  
http://localhost:8080/api/customer_account/  
http://localhost:8080/api/fund_transfer/  

-- tested on my MBP --