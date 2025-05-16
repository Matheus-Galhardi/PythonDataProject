import psycopg2
from AppUi import *

host = "localhost"
port = "5432"
database = "Main"
user = "postgres"
password = "36366331"
conn = None
cursor = None

nome = ""

def setup_students_data_base():
    try:
        global conn
        global cursor

        conn = psycopg2.connect (
                host = host,
                port = port,
                database = database,
                user = user,
                password = password,
            )
        cursor = conn.cursor()

        #cursor.execute("DROP TABLE IF EXISTS students")

        create_students = '''CREATE TABLE IF NOT EXISTS students (
                        id SERIAL PRIMARY KEY,
                        name VARCHAR(40) NOT NULL)'''
        cursor.execute(create_students)
        conn.commit()
    except (Exception, psycopg2.Error) as error:
        print(error)

def setup_admins_data_base():
    try:
        global conn
        global cursor

        conn = psycopg2.connect (
                host = host,
                port = port,
                database = database,
                user = user,
                password = password,
            )
        cursor = conn.cursor()

        #cursor.execute("DROP TABLE IF EXISTS students")

        create_students = '''CREATE TABLE IF NOT EXISTS admins (
                        id SERIAL PRIMARY KEY,
                        name VARCHAR(40) NOT NULL)'''
        cursor.execute(create_students)
        conn.commit()
    except (Exception, psycopg2.Error) as error:
        print(error)


def sign_in():
    nome = login_cred
    try:
        cursor = conn.cursor()
        insert_students = "INSERT INTO students(name) VALUES(%s)"
        cursor.execute(insert_students, [nome])
        conn.commit()
    except Exception as error:
        print(error)

def close_all():
    if cursor is not None:
        cursor.close()
    if conn is not None:
        conn.close()