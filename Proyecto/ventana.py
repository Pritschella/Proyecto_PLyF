'''
Created on 24 may. 2021

@author: prits
'''

import tkinter as tk
from tkinter import messagebox as MB
from tkinter import ttk
from tkinter import PhotoImage
import conexion as con


#Creacion ventana y Configuracion
ventana = tk.Tk()
ventana.title("Menu de Sistema de EMPLEADOS")
ventana.geometry("1000x600")
ventana.configure(bg="azure")

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
numEmpleadoCaja = tk.Entry(ventana)
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
btnAlta=tk.Button(ventana, text="Realizar ALTA", width=15, command=lambda: obtenerDatos())
btnAlta.place(x=400, y=75)
btnBaja=tk.Button(ventana, text="Realizar BAJA", width=15, command=lambda: obtenerNumEmpleado())
btnBaja.place(x=400, y=105)
btnCambio=tk.Button(ventana, text="Realizar CAMBIOS", width=15, command=lambda: obtenerDatos())
btnCambio.place(x=400, y=135)
btnLimpiar=tk.Button(ventana, text="Limpiar", width=15, command=lambda: limpiar())
btnLimpiar.place(x=400, y=165)
btnLimpiar=tk.Button(ventana, text="Obtener", width=15, command=lambda: sacar())
btnLimpiar.place(x=400, y=195)

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

lb.place(x=10, y=280, width = 600, height=150)

def sacar():
    try:
        seleccionado = lb.curselection()[0]
        numEmpleado = lb.item(seleccionado, option="text")
        cargar(numEmpleado)
    except Exception as e:
        MB.showerror("Error", "Seleccione un registro de la tabla")

def actualizarLB(lb):
    return lb


def cargar(numEmpleado):
    limpiar()
    lista = con.DataBase().select_one(numEmpleado)
    numEmpleadoCaja.insert(0, lista[0])
    fNacimientoCaja.insert(0, lista[1])
    nombreCaja.insert(0, lista[2])
    apellidoCaja.insert(0, lista[3])
    generoCaja.insert(0, lista[4])
    fContratacionCaja.insert(0, lista[5])

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
def obtenerDatos():
    strNumEmpleado.set(numEmpleadoCaja.get())
    strFNacimiento.set(fNacimientoCaja.get())
    strNombre.set(nombreCaja.get())
    strApellido.set(apellidoCaja.get())
    strGenero.set(generoCaja.get())
    strFContratacion.set(fContratacionCaja.get())
    strSalario.set(salarioCaja.get())
    strNomDepartamento.set(nomDepartamentoCaja.get())
    
    if not strNumEmpleado.get() or not strFNacimiento.get() or not strNombre.get() or not strApellido.get() or not strGenero.get() or not strFContratacion.get() or not strSalario.get() or not strNomDepartamento.get():
        MB.showerror("Error", "Faltan Datos por llenar")
    elif not strNumEmpleado.get().isdigit() or not strSalario.get().isdigit():
        MB.showerror("Error", "Numero de empleado y salario deben llevar solo NUMEROS")
    else:
        realizarAlta(strNumEmpleado.get(), strFNacimiento.get(), strNombre.get(), strApellido.get(), strGenero.get(), strFContratacion.get())
        MB.showinfo("Exito", "Alta/Cambio Realizado")
        actualizarT()
    
def actualizarT():
    lb = ttk.Treeview(ventana,columns=("numEmpleado","fNacimiento", "name", "last_name","gender","hire_date"), show='headings')
    lb.heading("numEmpleado", text="Numero de empleado")
    lb.column("numEmpleado", width=45)
    lb.heading("fNacimiento", text="Fecha de nacimiento")
    lb.column("fNacimiento", width=45)
    lb.heading("name", text="Nombre")
    lb.column("name", width=45)
    lb.heading("last_name",text="Apellidos")
    lb.column("last_name", width=45)
    lb.heading("gender",text="Genero")
    lb.column("gender", width=45)
    lb.heading("hire_date",text="Contratacion")
    lb.column("hire_date", width=45)
    items = con.DataBase().select_all()
    
    for j in items:
        lb.insert('', tk.END, values =(j[0], j[1], j[2],j[3],j[4],j[5]))

    lb.place(x=10, y=280, width = 600, height=150)
    return lb
lb = actualizarT()

def obtenerNumEmpleado():
    strNumEmpleado.set(numEmpleadoCaja.get())
    if strNumEmpleado.get():
        con.DataBase().baja(strNumEmpleado.get())
        actualizarT()
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

def realizarAlta(EN,BD, FN, LN,G,HD):
    con.DataBase().alta(EN, BD, FN, LN, G, HD)
#----------------
ventana.mainloop()