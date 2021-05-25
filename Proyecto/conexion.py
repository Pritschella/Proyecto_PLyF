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
        sql = "SELECT emp_no, birth_date FROM employees WHERE emp_no = '{}'".format(numEmpleado)
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