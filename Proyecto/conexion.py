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
        sql = "SELECT * FROM employees WHERE emp_no = '%d'"%(numEmpleado,)
        try:
            self.cursor.execute(sql)
            empleado = self.cursor.fetchone()
            
        except Exception as e:
            raise e
        return empleado
    
    def select_empleadosBD(self, fecha):
        sql = "SELECT * FROM employees WHERE birth_date like '%"+fecha+"%'"
        try:
            self.cursor.execute(sql)
            empleado = self.cursor.fetchall()
            print (empleado)
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
    
    def alta(self, EN, BD, FN, LN, G, HD, S, D):
        fecha = HD.substringData(0-3)
        print(fecha)
        fecha2=fecha+1
        strfecha= fecha2+""+HD.substringData(4-9)
        sql = "Insert into employees (emp_no, birth_date, first_name, last_name, gender, hire_date) VALUES ('%d','%s','%s','%s','%s','%s')"%(EN, BD, FN, LN, G, HD,)
        
        sql2="Insert into dept_emp values('%d', '%s')"%(EN, strfecha)
        try:
            self.cursor.execute(sql)
            self.connection.commit()
        except Exception as e:
            raise e
    
    def actualizar(self,EN,BD,FN, LN, G, HD):
        sql="Update employees set birth_date = '%s', first_name='%s', last_name='%s', gender='%s', hire_date='%s' where emp_no='%d'"%(BD, FN,LN,G,HD,EN)
        try:
            self.cursor.execute()
            self.connection.commit()
        except Exception as e:
            raise e
        
        
    def baja(self, numEmpleado):
        sql = "Delete from employees where emp_no = '%d'"%(numEmpleado,)
        sql2 = "Delete from dept_emp where emp_no = '%d'"%(numEmpleado,)
        sql3 = "Delete from departments where emp_no = '%d'"%(numEmpleado,)
        try:
            #self.cursor.execute(sql2)
            #self.cursor.execute(sql3)
            self.cursor.execute(sql)
            self.connection.commit()
        except Exception as e:
            raise e

#database=DataBase()