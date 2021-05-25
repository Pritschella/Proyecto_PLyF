'''
Created on 22 may. 2021

@author: prits
'''

import pymysql

class DataBase:
    def __init__(self):
        self.connection = pymysql.connect(
            host="localhost",
            user = "root",
            password="berenice",
            db="employees")
        
        self.cursor = self.connection.cursor()
        
        print("Conexion exitosa")
        
    def select_one(self, numEmpleado):
        sql = "SELECT * FROM employees WHERE emp_no = '{}'".format(numEmpleado)
        try:
            self.cursor.execute(sql)
            empleado = self.cursor.fetchone()
            
        except Exception as e:
            raise e
        return empleado
    
    def select_all(self):
        sql = 'SELECT * FROM employees'
        try:
            self.cursor.execute(sql)
            empleado = self.cursor.fetchall()
            
        except Exception as e:
            raise e
        return empleado
    def alta(self, EN, BD, FN, LN, G, HD):
        sql = "Insert into employees (emp_no, birth_date, first_name, last_name, gender, hire_date) VALUES ('{}','{}','{}','{}','{}','{}')".format(EN, BD, FN, LN, G, HD)
        try:
            self.cursor.execute(sql)
            self.connection.commit()
        except Exception as e:
            raise e
        
    def baja(self, numEmpleado):
        sql = "Delete from employees where emp_no = {}".format(numEmpleado)
        try:
            self.cursor.execute(sql)
            self.connection.commit()
        except Exception as e:
            raise e

#database=DataBase()