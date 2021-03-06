'''
Created on 20 may. 2021

@author: prits
'''

import tkinter as tk
from tkinter import messagebox as MB
from tkinter import PhotoImage
import conexion as con

#Creacion login y configuracion
login = tk.Tk()
login.title("Login")
login.geometry("300x300")
login.configure(bg="SkyBlue")

#Titulo
titulo = tk.Label(login, text="SISTEMA DE EMPLEADOS", bg="SkyBlue", font=("Helvetica", 16))
titulo.pack(fill=tk.X)
imagen = PhotoImage(file="login.png")
img = tk.Label(login, imag = imagen).place(x=130, y=50)
etiqueta=tk.Label(login, text="Llena los siguientes campos...", bg = "SkyBlue", font=("Arial", 12))
etiqueta.place(x=50, y=100)

#etiquetas
usLabel = tk.Label(login, text="Usuario", bg = "SkyBlue")
usLabel.place(x=20, y=140)
conLabel = tk.Label(login, text="Password", bg="SkyBlue")
conLabel.place(x=20, y=180)

#cajas
usCaja = tk.Entry(login)
usCaja.place(x=100, y=140)
conCaja = tk.Entry(login, show="*")
conCaja.place(x=100, y =180)

#boton
btnIniciar = tk.Button(login, text="Iniciar", width=20, command=lambda: obtenerDatos())
btnIniciar.place(x=90, y=250)


#vars
strUs=tk.StringVar()
strCon=tk.StringVar()

#metodos
def obtenerDatos():
    strUs.set(usCaja.get())
    strCon.set(conCaja.get())
    if not strUs.get() or not strCon.get():
        MB.showerror("Error", "Llena los campos")
    elif not strUs.get().isalpha():
        MB.showerror("Error", "Usuario Solo Puede Llevar LETRAS")
    else:
        lleno = con.DataBase().validarUsuario(strUs.get(), strCon.get())
        
        if (lleno):
            abrirVentana()
        else:
            MB.showerror("Error", "Usuario o Contrasena Incorrectos")

def abrirVentana():
    login.destroy()
    import ventana

#--------------------------
login.mainloop()
 
 