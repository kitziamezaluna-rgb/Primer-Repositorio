#MEZA LUNA KITZIA SOPHIA
#17/10/2025
#CBTIS89
#Programacion 3°B turno matutino 
#Lista desplegable combo box de colores
import tkinter as tk
from tkinter import ttk

ventana=tk.Tk()
ventana.title(" LISTA DESPLEGABLE COMBO BOX")
ventana.geometry("300x200")
#color de fondo para la ventana
ventana.configure(bg="#B7FAF4")

etiqueta=tk.Label(ventana,text="elige una opcion",font=("ALEGRIAN",12,"bold"),fg="#3758B3")
etiqueta.pack(pady=10)

opciones=["ROJO","VERDE", "AZUL","AMARILLO","MORADO"]

ComboColores=ttk.Combobox(ventana,values=opciones,state="readonly")
ComboColores.pack(pady=5)

def mostrar_seleccion(event):
    seleccion=ComboColores.get() #obtiene el valor seleccionado
    etiqueta_resultado.config(text=f"SELECCIONASTE: {seleccion}",bg="#979797")
    if seleccion=="ROJO":
        etiqueta_color.configure(bg="#FF0000")
        etiqueta_resultado.configure(fg="#f70505")
    elif seleccion=="VERDE": 
        etiqueta_color.configure(bg="#2d6e27")
        etiqueta_resultado.configure(fg="#208644")
    elif seleccion=="AZUL":
        etiqueta_color.configure(bg="#1E1263")
        etiqueta_resultado.configure(fg="#0f1855")
    elif seleccion=="AMARILLO":
        etiqueta_color.configure(bg="#fce30a")
        etiqueta_resultado.configure(fg="#ffea05")
    elif seleccion=="MORADO":
        etiqueta_color.configure(bg="#bc0dcc")
        etiqueta_resultado.configure(fg="#8b246e")
ComboColores.bind("<<ComboboxSelected>>",mostrar_seleccion)

etiqueta_resultado=tk.Label(ventana, text="")
etiqueta_resultado.pack(pady=5)
etiqueta_color=tk.Label(ventana,width=10, height=3)
etiqueta_color.pack(pady=10)
etiqueta_color

ventana.mainloop()