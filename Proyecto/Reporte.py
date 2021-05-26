import itertools
from random import randint
import webbrowser as wb
from reportlab.pdfgen.canvas import *
from statistics import mean
from reportlab.lib.pagesizes import A4
from reportlab.lib.fonts import *
import conexion as con
from reportlab.pdfgen import canvas

def grouper(iterable,n):
    args = [iter(iterable)]*n
    return itertools.zip_longest(*args)

def export_to_pdf():
    
    data = [("emp_no", "birth_date","first_name", "last_name", "gender", "hire_date")]
    registros = con.DataBase().select_empleadosBD("1960")
    
    for row in registros:
        data.append((str(row[0]),str(row[1]),str(row[2]),str(row[3]),str(row[4]),str(row[5])))
    c = canvas.Canvas("Reportes/empleados.pdf", pagesize=A4)

    text=c.beginText(10,810,None)
    text.setFont("Times-Roman",12)
    text.textLine("Employees- Reporte empleados nacidos en ela;o 1960")
    c.drawText(text)
    w,h = A4
    max_rows_per_page = 40
    
    x_offset = 50
    y_offset = 50
    
    padding=15
    
    xlist = [x+ x_offset for x in [0,60,200,250,300,350,400,480]]
    ylist = [h - y_offset - i*padding for i in range(max_rows_per_page + 1)]

    for rows in grouper(data, max_rows_per_page):
        rows = tuple(filter(bool, rows))
        c.grid(xlist, ylist[:len(rows) + 1])
        for y, row in zip(ylist[:-1], rows):
            for x, cell in zip(xlist, row):
                c.drawString(x + 2, y - padding + 3, str(cell))
        c.showPage()

    c.save()
    
    #wb.open_new("www.google.com")
    wb.open_new("C:\\Users\\prits\\git\\repository\\Proyecto_PLyF\\Reportes\\empleados.pdf")
    
    
#export_to_pdf()