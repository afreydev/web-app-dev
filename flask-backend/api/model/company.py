import functools
import db
import pymysql

def get_companies():
    con = db.get_connection()
    cursor = con.cursor(pymysql.cursors.DictCursor)
    try:
        sql="SELECT * FROM companies"
        cursor.execute(sql)
        ret = cursor.fetchall()
        print(ret)
        return ret
    finally:
        con.close()

def get_company(company_id):
    con = db.get_connection() 
    cursor = con.cursor(pymysql.cursors.DictCursor)
    ret={}
    try:
        sql="SELECT * FROM companies WHERE id = {}".format(company_id)
        cursor.execute(sql)
        ret = cursor.fetchone()
        return ret
    finally:
        con.close()

def get_company_by_name(company_name):
    con = db.get_connection() 
    cursor = con.cursor(pymysql.cursors.DictCursor)
    ret={}
    try:
        sql="SELECT * FROM companies WHERE name = '{}'".format(company_name)
        print(sql)
        cursor.execute(sql)
        ret = cursor.fetchone()
        return ret
    finally:
        con.close()

def create_company(name, description):
    con = db.get_connection()
    cursor = con.cursor()
    try:
        sql="INSERT INTO companies(name, description) VALUES('{}','{}')".format(name, description)
        print(sql)
        cursor.execute(sql)
        con.commit()
        id_org = cursor.lastrowid
        return {"message":"OK", "id": id_org}
    finally:
        con.close()

def update_company(name, description, company_id):
    con = db.get_connection()
    cursor = con.cursor()
    try:
        sql="UPDATE companies set name='{0}', description='{1}' WHERE id = {2}".format(name, description, company_id)
        print(sql)
        cursor.execute(sql)
        con.commit()
        return {"message":"OK"}
    finally:
        con.close()

def delete_company(company_id):
    con = db.get_connection()
    cursor = con.cursor()
    try:
        sql="DELETE FROM companies WHERE id = {}".format(company_id)
        cursor.execute(sql)
        con.commit()
        return {"message":"OK"}
    finally:
        con.close()
