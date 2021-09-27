import os
import urllib

host_server = os.environ.get('POSTGRES_HOST', 'localhost')
db_server_port = urllib.parse.quote_plus(str(os.environ.get('POSTGRES_PORT', '15432')))
database_name = os.environ.get('POSTGRES_DB', 'airbnb')
db_username = urllib.parse.quote_plus(str(os.environ.get('POSTGRES_USER', 'pgsync')))
db_password = urllib.parse.quote_plus(str(os.environ.get('POSTGRES_PASSWORD', 'PLEASE_CHANGE_ME')))


DATABASE_URL = 'postgresql://{}:{}@{}:{}/{}?sslmode=prefer'.format(db_username,db_password, host_server, db_server_port, database_name)
ELASTICSEARCH_URL = f"{os.environ.get('ELASTICSEARCH_HOST', 'localhost')}:{os.environ.get('ELASTICSEARCH_PORT', '9201')}"
