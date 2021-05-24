'''
Created on 20 may. 2021

@author: prits
'''

import tkinter as tk
from tkinter import messagebox as MB

#Creacion login y configuracion
login = tk.Tk()
login.title("Login")
login.geometry("3000x300")
login.configure(bg="SkyBlue")

#Titulo
titulo = tk.Label(login, text="SISTEMA DE EMPLEADOS", bg="SkyBlue", font=("Helvetica", 16))
titulo.pack(fill=tk.X)
etiqueta=tk.Label(login, text="Llena los siguientes campos", bg = "SkyBlue")
etiqueta.pack()

#etiquetas
usLabel = tk.Label(login, text="Usuario", bg = "SkyBlue")
usLabel.place(x=20, y=80)
conLabel = tk.Label(login, text="Password", bg="SkyBlue")
conLabel.place(x=20, y=180)

#cajas
usCaja = tk.Entry(login)
usCaja.place(x=100, y=80)
conCaja = tk.Entry(login, show="*")
conCaja.place(x=100, y =180)

#boton
btnIniciar=tk.Button(login, text="        Iniciar        ", height=2,  command=lambda: obtenerDatos())
btnIniciar.place(x=110, y=250)

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
        if strUs.get()=="a" and strCon.get()=="a":
            abrirVentana()
        else:
            MB.showerror("Error", "Usuario o Contrasena Incorrectos")

def abrirVentana():
    login.destroy()

#--------------------------
login.mainloop()
 
 