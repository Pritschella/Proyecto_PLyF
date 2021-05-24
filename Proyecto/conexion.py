'''
Created on 22 may. 2021

@author: prits
'''

import pymysql

try:
    conexion = pymysql.connect(host='localhost',
                               user='root',
                               password='berenice',
                               db='employees')
    
    print("Conexion correcta")

except(pymysql.err.OperationalError, pymysql.err.InternalError) as e:
    print("Ocurrio un error al conectar: ", e)