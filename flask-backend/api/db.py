from decouple import config
import pymysql

MYSQL_HOST = config('MYSQL_HOST', default='localhost')
MYSQL_USER = config('MYSQL_USER', default='root')
MYSQL_PASSWORD = config('MYSQL_PASSWORD', default='rootroot')
MYSQL_DATABASE = config('MYSQL_DATABASE', default='db_companies')

def get_connection():
    return pymysql.connect(
        host=MYSQL_HOST,
        user=MYSQL_USER,
        password=MYSQL_PASSWORD,
        database=MYSQL_DATABASE
    )
