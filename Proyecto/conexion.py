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
    
    def buscar(self, Busqueda):
        sql ="Select * from employees where first_name like '%"+Busqueda+"%' OR last_name like '%"+Busqueda+"%'" 
        try:
            self.cursor.execute(sql)
            empleado = self.cursor.fetchall()
        except Exception as e:
            raise e
        return empleado   
    
    def ultimoEN(self):
        sql = "SELECT MAX(emp_no) AS emp_no FROM employees"
        try:
            self.cursor.execute(sql)
            empleado = self.cursor.fetchone()
            
        except Exception as e:
            raise e
        return empleado
    
        
    def select_one(self, numEmpleado):
        sql = "SELECT * FROM employees WHERE emp_no = '%s'"%(numEmpleado,)
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
    
    def alta(self, EN, BD, FN, LN, G, HD):
        #fecha = HD.substringData(0-3)
        #print(fecha)
        #fecha2=fecha+1
        #strfecha= fecha2+""+HD.substringData(4-9)
        sql = "Insert into employees (emp_no, birth_date, first_name, last_name, gender, hire_date) VALUES ('{}','{}','{}','{}','{}','{}')".format(EN, BD, FN, LN, G, HD,)
        
        #sql2="Insert into dept_emp values('%d', '%s')"%(EN, strfecha)
        try:
            self.cursor.execute(sql)
            self.connection.commit()
        except Exception as e:
            raise e
    
    def validarUsuario(self, user, passw):
        sql = "SELECT * FROM login Where usuario = '%s' AND password = '%s'"%(user, passw)
        
        try:
            self.cursor.execute(sql)
            usuario = self.cursor.fetchall()
        except Exception as e:
            raise e
        return usuario
    
    def actualizar(self,EN,BD,FN, LN, G, HD):
        sql="Update employees set birth_date = '%s', first_name='%s', last_name='%s', gender='%s', hire_date='%s' where emp_no='%s'"%(BD, FN,LN,G,HD,EN)
        try:
            self.cursor.execute(sql)
            self.connection.commit()
        except Exception as e:
            raise e
        
    def select_depa(self, ndepa):
        sql = "select * from departments where dept_name = '%s'"%(ndepa)
        try: 
            self.cursor.execute(sql)
            depa = self.cursor.fetchone()
        except Exception as e:
            raise e
        
    def update_dept(self, EN, DN, FD, TD):
        sql = "Update dept_emp dept_no='%s', from_date='%s', to_date='%s' where emp_no='%s'"%(EN , DN, FD, TD)
        try:
            self.cursor.execute(sql)
            self.connection.commit()
        except Exception as e:
            raise e
    
    def update_salary(self, EN, S, FD, TD):
        sql = "update salaries salary='%s', from_date='%s', to_date='%s' where emp_no='%s'"%(EN, S, FD, TD)
        try:
            self.cursor.execute(sql)
            self.connection.commit()
        except Exception as e:
            raise e
        
    def insert_dept(self, EN, DN, FD, TD):
        sql = "INSERT INTO dept_emp (emp_no, dept_no, from_date, to_date) values ('%s', '%s', '%s', '%s')"%(EN , DN, FD, TD)
        try:
            self.cursor.execute(sql)
            self.connection.commit()
        except Exception as e:
            raise e
    
    def insert_salary(self, EN, S, FD, TD):
        sql = "INSERT INTO salaries (emp_no, salary, from_date, to_date) values('%s','%s', '%s','%s')"%(EN, S, FD, TD)
        try:
            self.cursor.execute(sql)
            self.connection.commit()
        except Exception as e:
            raise e
                
    def baja(self, numEmpleado):
        sql = "Delete from employees where emp_no = '%s'"%(numEmpleado,)
        #sql2 = "Delete from dept_emp where emp_no = '%d'"%(numEmpleado,)
        #sql3 = "Delete from departments where emp_no = '%d'"%(numEmpleado,)
        try:
            #self.cursor.execute(sql2)
            #self.cursor.execute(sql3)
            self.cursor.execute(sql)
            self.connection.commit()
        except Exception as e:
            raise e
#fecha = "1990-12-12"
#fechacam = fecha.substring(0-3)
#print(fechacam)
#database=DataBase()