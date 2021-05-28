'''
Created on 24 may. 2021

@author: prits
'''

import tkinter as tk
from tkinter import messagebox as MB, Menu
from tkinter import ttk
from tkinter import PhotoImage
import conexion as con
import Reporte
from datetime import timedelta, date
from datetime import datetime
from plistlib import _date_to_string
from gc import disable
from tkinter.constants import NORMAL

#Creacion ventana y Configuracion
ventana = tk.Tk()
ventana.title("Menu de Sistema de EMPLEADOS")
ventana.geometry("1000x600")
ventana.configure(bg="azure")

#menu bar
#menubar = Menu(ventana, font=("Monsterrant",16))
#ventana.config(menu=menubar)
#reportes = Menu(menubar, tearoff=0)
#reportes.add_command(label="Generar Reportes")
#menubar.add_cascade(label="Reportes", menu=reportes,command=reportes)


def reportes():
    print("Generando reporte")
    Reporte.export_to_pdf()


#Titulos
titulo = tk.Label(ventana, text="Sistema de EMPLEADOS", bg = "azure", font=("Helvetica", 16))
etiqueta = tk.Label(ventana, text="Bienvenido al Sistema ABCC de Empleados", bg="azure")
titulo.pack(fill=tk.X)
etiqueta.pack()


#Etiquetas
numEmpleadoLabel = tk.Label(ventana, text="Ingresa No. de Empleado: ", bg="azure")
numEmpleadoLabel.place(x=30, y=60)
fNacimientoLabel = tk.Label(ventana, text="Ingresa Fecha de Nacimiento: ", bg="azure")
fNacimientoLabel.place(x=30, y=85)
nombreLabel = tk.Label(ventana, text="Ingresa Nombre: ", bg="azure")
nombreLabel.place(x=30, y=110)
apellidoLabel = tk.Label(ventana, text="Ingresa Apellido: ", bg="azure")
apellidoLabel.place(x=30, y=135)
generoLabel = tk.Label(ventana, text="Selecciona genero: ", bg="azure")
generoLabel.place(x=30, y=160)
fContratacionLabel = tk.Label(ventana, text="Ingresa fecha de contratacion", bg="azure")
fContratacionLabel.place(x=30, y=185)
salarioLabel = tk.Label(ventana, text="Ingresa el salario: ", bg="azure")
salarioLabel.place(x=30, y=210)
nomDepartamentoLabel = tk.Label(ventana, text="Selecciona el Nombre de Departamento:", bg="azure")
nomDepartamentoLabel.place(x=30, y=235)


#Cajas
numEmpleadoCaja = tk.Entry(ventana, state="normal")
numEmpleadoCaja.place(x=250, y=60)
fNacimientoCaja = tk.Entry(ventana)
fNacimientoCaja.place(x=250, y=85)
nombreCaja = tk.Entry(ventana)
nombreCaja.place(x=250, y=110)
apellidoCaja =  tk.Entry(ventana)
apellidoCaja.place(x=250, y=135)
generoCaja = ttk.Combobox(ventana, state="readonly", width=17)
generoCaja["values"] = ["M", "F"]
generoCaja.place(x=250, y=160)
fContratacionCaja = tk.Entry(ventana)
fContratacionCaja.place(x=250, y=185)
salarioCaja = tk.Entry(ventana)
salarioCaja.place(x=250, y=210)
nomDepartamentoCaja = ttk.Combobox(ventana, state="readonly", width=17)
nomDepartamentoCaja["values"] = ["Customer Service", "Development", "Finance", "Human Resources",
                                 "Marketing", "Production", "Quality Management", "Research", "Sales"]
nomDepartamentoCaja.place(x=250, y=235)



#botones
btnAlta=tk.Button(ventana, text="Realizar ALTA", width=15, command=lambda: obtenerDatosA())
btnAlta.place(x=400, y=75)
btnBaja=tk.Button(ventana, text="Realizar BAJA", width=15, command=lambda: obtenerNumEmpleado())
btnBaja.place(x=400, y=105)
btnCambio=tk.Button(ventana, text="Realizar CAMBIOS", width=15, command=lambda: obtenerDatos())
btnCambio.place(x=400, y=135)
btnLimpiar=tk.Button(ventana, text="Limpiar", width=15, command=lambda: limpiar())
btnLimpiar.place(x=400, y=165)
btnObtener=tk.Button(ventana, text="Obtener", width=15, command=lambda: sacar())
btnObtener.place(x=400, y=195)
icopdf = PhotoImage(file='pdf.png')
btnPDF=tk.Button(ventana, text="Limpiar", image=icopdf, width=30, command=lambda: reportes())
btnPDF.place(x=650, y=120)

#Listbox
lb = ttk.Treeview(ventana, columns=("numEmpleado","fNacimiento", "name", "last_name","gender","hire_date"), show='headings')
lb.heading("numEmpleado", text="Numero de empleado")
lb.heading("fNacimiento", text="Fecha de nacimiento")
lb.heading("name", text="Nombre")
lb.heading("last_name",text="Apellidos")
lb.heading("gender",text="Genero")
lb.heading("hire_date",text="Contratacion")
items = con.DataBase().select_all()
for j in items:
    lb.insert('', tk.END, values =(j[0], j[1], j[2],j[3],j[4],j[5]))
    if j == 50:
        break

lb.place(x=10, y=280, width = 900, height=150)

def sacar():
    try:
        seleccionado = lb.selection()[0]
        print(seleccionado)
        numEmpleado = lb.item(seleccionado, option='values') 
        print(numEmpleado)
        cargar(numEmpleado)
    except Exception as e:
        MB.showerror("Error", "Seleccione un registro de la tabla")

def actualizarLB(lb):
    return lb

def onReturn(event):
    if(con.DataBase().buscardept(busquedacaja.get())):
        items =con.DataBase().buscardept(busquedacaja.get())
        print(items)
        lb.delete(*lb.get_children())
        for j  in items :
            lb.insert('', tk.END, values =(j[0], j[1], j[2],j[3],j[4],j[5]))
        

        lb.place(x=10, y=280, width = 900, height=150)
        lb.selection_remove()
        return lb
    
busquedacaja = ttk.Entry(ventana)
busquedacaja.bind('<Key>', onReturn)
busquedacaja.place(x=400, y=220)

def cargar(numEmpleado):
    limpiar()
    #lista = con.DataBase().select_one(numEmpleado)
    print(numEmpleado[0])
    numEmpleadoCaja.insert(0, numEmpleado[0])
    fNacimientoCaja.insert(0, numEmpleado[1])
    nombreCaja.insert(0, numEmpleado[2])
    apellidoCaja.insert(0, numEmpleado[3])
    #generoCaja(0, numEmpleado[4])
    generoCaja.insert(0, numEmpleado[4])
    fContratacionCaja.insert(0, numEmpleado[5])

#Variables
strNumEmpleado = tk.StringVar()
strFNacimiento = tk.StringVar()
strNombre = tk.StringVar()
strApellido = tk.StringVar()
strGenero = tk.StringVar()
strFContratacion = tk.StringVar()
strSalario = tk.StringVar()
strNomDepartamento = tk.StringVar()


#Funciones
def obtenerDatosA():
    strNumEmpleado.set(numEmpleadoCaja.get())
    strFNacimiento.set(fNacimientoCaja.get())
    strNombre.set(nombreCaja.get())
    strApellido.set(apellidoCaja.get())
    strGenero.set(generoCaja.get())
    strFContratacion.set(fContratacionCaja.get())
    strSalario.set(salarioCaja.get())
    strNomDepartamento.set(nomDepartamentoCaja.get())
    
    #if not strFNacimiento.get() or not strNombre.get() or not strApellido.get() or not strGenero.get() or not strFContratacion.get() or not strSalario.get() or not strNomDepartamento.get():
     #   MB.showerror("Error", "Faltan Datos por llenar")
    #elif not strSalario.get().isdigit():
     #   MB.showerror("Error", "salario debe llevar solo NUMEROS")
        
    #elif strNombre.get().isdigit() or strApellido.get().isdigit():
     #   MB.showerror("Error", "Nombre y/o apellidos deben llevar solo LETRAS")
     
    if not strFNacimiento.get():
        MB.showerror("Error", "Ingrese la fecha de nacimiento")
    elif not strNombre.get():
        MB.showerror("Error", "Ingrese un Nombre")
    elif strNombre.get().isdigit():
        MB.showerror("Error", "El nombre debe llevar solo LETRAS")
    elif not strApellido.get():
        MB.showerror("Error", "Ingrese un Apellido")
    elif strApellido.get().isdigit():
        MB.showerror("Error", "El Apellido debe llevar solo LETRAS")
    elif not strGenero.get():
        MB.showerror("Error", "Falta seleccionar genero")
    elif not strFContratacion.get():
        MB.showerror("Error", "Ingrese la fecha de contratacion")
    elif not strSalario.get():
        MB.showerror("Error", "Ingrese el salario")
    elif not strSalario.get().isdigit():
        MB.showerror("Error", "El salario debe llever solo NUMEROS")   
    elif not strNomDepartamento.get():
        MB.showerror("Error", "Seleccione Nombre de Departamento")
     
        
    else:
        try:
            fechaC = strFContratacion.get()
            fechaN = strFNacimiento.get()
            datetime.strptime(fechaC, '%Y-%m-%d')
            datetime.strptime(fechaN, '%Y-%m-%d')
            
            
            realizarAlta(strNumEmpleado.get(), strFNacimiento.get(), strNombre.get(), strApellido.get(), strGenero.get(), strFContratacion.get(), strSalario.get(), strNomDepartamento.get())
            MB.showinfo("Exito", "Alta Realizado")
            actualizarT()
        except ValueError:
            MB.showerror("Error", "Formato erroneo de fecha de nacimiento o fecha de contratacion debe ser YYYY-MM-DD")

def obtenerDatos():
    strNumEmpleado.set(numEmpleadoCaja.get())
    strFNacimiento.set(fNacimientoCaja.get())
    strNombre.set(nombreCaja.get())
    strApellido.set(apellidoCaja.get())
    strGenero.set(generoCaja.get())
    strFContratacion.set(fContratacionCaja.get())
    strSalario.set(salarioCaja.get())
    strNomDepartamento.set(nomDepartamentoCaja.get())
    
    if not strFNacimiento.get():
        MB.showerror("Error", "Ingrese la fecha de nacimiento")
    elif not strNombre.get():
        MB.showerror("Error", "Ingrese un Nombre")
    elif strNombre.get().isdigit():
        MB.showerror("Error", "El nombre debe llevar solo LETRAS")
    elif not strApellido.get():
        MB.showerror("Error", "Ingrese un Apellido")
    elif strApellido.get().isdigit():
        MB.showerror("Error", "El Apellido debe llevar solo LETRAS")
    elif not strGenero.get():
        MB.showerror("Error", "Falta seleccionar genero")
    elif not strFContratacion.get():
        MB.showerror("Error", "Ingrese la fecha de contratacion")
    elif not strSalario.get():
        MB.showerror("Error", "Ingrese el salario")
    elif not strSalario.get().isdigit():
        MB.showerror("Error", "El salario debe llever solo NUMEROS")   
    elif not strNomDepartamento.get():
        MB.showerror("Error", "Seleccione Nombre de Departamento")
        

    
    #if not strFNacimiento.get() or not strNombre.get() or not strApellido.get() or not strGenero.get() or not strFContratacion.get() or not strSalario.get() or not strNomDepartamento.get():
        #MB.showerror("Error", "Faltan Datos por llenar")
    #elif not strSalario.get().isdigit():
        #MB.showerror("Error", "salario debe llevar solo NUMEROS")
        
    #elif strNombre.get().isdigit() or strApellido.get().isdigit():
        #MB.showerror("Error", "Nombre y/o apellidos deben llevar solo LETRAS")
        
    else:
        try:
            fechaC = strFContratacion.get()
            fechaN = strFNacimiento.get()
            datetime.strptime(fechaC, '%Y-%m-%d')
            datetime.strptime(fechaN, '%Y-%m-%d')
            realizarCambio(strNumEmpleado.get(), strFNacimiento.get(), strNombre.get(), strApellido.get(), strGenero.get(), strFContratacion.get(), strSalario.get(), strNomDepartamento.get())
            MB.showinfo("Exito", "Cambio Realizado")
            actualizarT()
        except ValueError:
            MB.showerror("Error", "Formato erroneo de fecha de nacimiento o fecha de contratacion el formato es YYYY-MM-DD")
        
    
def actualizarT():
    #lb = ttk.Treeview(ventana,columns=("numEmpleado","fNacimiento", "name", "last_name","gender","hire_date"), show='headings')
    #lb.heading("numEmpleado", text="Numero de empleado")
    #lb.column("numEmpleado", width=45)
    #lb.heading("fNacimiento", text="Fecha de nacimiento")
    #lb.column("fNacimiento", width=45)
    #lb.heading("name", text="Nombre")
    #lb.column("name", width=45)
    #lb.heading("last_name",text="Apellidos")
    #lb.column("last_name", width=45)
    #lb.heading("gender",text="Genero")
    #lb.column("gender", width=45)
    #lb.heading("hire_date",text="Contratacion")
    #lb.column("hire_date", width=45)
    lb.delete(*lb.get_children())
    items = con.DataBase().select_all()
    
    for j in items:
        lb.insert('', tk.END, values =(j[0], j[1], j[2],j[3],j[4],j[5]))

    lb.place(x=10, y=280, width = 900, height=150)
    lb.selection_remove()
    return lb
#lb = actualizarT()

def obtenerNumEmpleado():
    strNumEmpleado.set(numEmpleadoCaja.get())
    if strNumEmpleado.get():
        con.DataBase().baja(strNumEmpleado.get())
        actualizarT()
        limpiar()
        MB.showinfo("Exito", "Baja Realizada")
    else:
        MB.showerror("Error", "Introduce un Numero de Empleado")
    
    
def imprimir():
    print(strNumEmpleado.get()+strGenero.get())
    
def limpiar():
    numEmpleadoCaja.delete(0, tk.END)
    fNacimientoCaja.delete(0, tk.END)
    nombreCaja.delete(0, tk.END)
    apellidoCaja.delete(0, tk.END)
    generoCaja.set("")
    fContratacionCaja.delete(0, tk.END)
    salarioCaja.delete(0, tk.END)
    nomDepartamentoCaja.set("")  

def realizarCambio(EN, BD, FN, LN,G,HD, S, D):
    ultimoEN = con.DataBase().ultimoEN()
    #f = HD.date ()
    #fechato = f.year() +1
    #DN = con.DataBase().select_depa(D)
    #con.DataBase().insert_salary(EN, S, HD, _date_to_string( fechato))
    #con.DataBase().insert_dept(EN, DN, HD, _date_to_string( fechato))
    con.DataBase().actualizar(EN, BD, FN, LN, G, HD)
    MB.showinfo("Exito", "Cambio Realizado")
    limpiar()

def realizarAlta(EN,BD, FN, LN,G,HD, S, D):
    altas = con.DataBase().select_one(EN)
    ultimoEN = con.DataBase().ultimoEN()
    #print("HD " +HD)
    #fechato =  HD +1
    #print(fechato)
    #DN = con.DataBase().select_depa(D)
    if(altas):
        MB.showinfo("Error", "El numero de empleado ya existe")
    else:
        #con.DataBase().insert_salary(EN, S, HD, _date_to_string( fechato))
        #con.DataBase().insert_dept(EN, DN, HD, _date_to_string( fechato))
        con.DataBase().alta(ultimoEN[0]+1, BD, FN, LN, G, HD)
        limpiar()
#----------------
ventana.mainloop()