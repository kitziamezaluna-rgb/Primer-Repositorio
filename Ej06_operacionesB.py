#MEZA LUNA KITZIA SOPHIA
#13/10/2025
#CBTIS89
#Programacion 3°B turno matutino 
#Agrega los botones 
# restar, multiplicar y dividir. 
# Usa en el mismo mensaje el resultado.
import tkinter as tk

def sumar():
   try:
      num1=float(entrada1.get())
      num2=float(entrada2.get())
      suma=num1+num2
      resultado.config(text=f"resultado: {suma}")
   except ValueError:
      resultado.config(text="Por favor, ingresa solo números")
#debo de tener cuidado con el acomodo de lineas o sangria 
def restar():
   try:
      num1=float(entrada1.get())
      num2=float(entrada2.get())
      resta=num1-num2
      resultado.config(text=f"resultado: {resta}")
   except ValueError:
      resultado.config(tex="porfavor ingresa solo numeros")

def multiplicar():
   try:
      num1=float(entrada1.get())
      num2=float(entrada2.get())
      multiplicar=num1*num2
      resultado.config(text=f"resultado {multiplicar}")
   except ValueError:
      resultado.config(text="porfavor ingresa solo numeros")

def dividir():
   try:
      num1=float(entrada1.get())
      num2=float(entrada2.get())
      dividir=num1/num2
      resultado.config(text=f"divicion {dividir}")
   except ValueError:
      resultado.config(text="ingrese solo numeros ")


# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Suma de dos números")
ventana.geometry("230x400")
# Crear los cuadros de texto
entrada1 = tk.Entry(ventana)
entrada2 = tk.Entry(ventana)
# Posicionar las entradas en la ventana
entrada1.pack(pady=5)
entrada2.pack(pady=5)

# Crear botón de suma
boton_sumar = tk.Button(ventana, text="Sumar", command=sumar)
boton_sumar.pack(pady=5)
boton_restar= tk.Button(ventana,text="restar",command=restar)
boton_restar.pack(pady=10)
boton_multiplicar=tk.Button(ventana,text="multiplicar",command=multiplicar)
boton_multiplicar.pack(pady=15)
boton_dividir=tk.Button(ventana,text="dividir",command=dividir)
boton_dividir.pack(pady=20)

# Crear etiqueta para mostrar el resultado
resultado = tk.Label(ventana, text="Resultado:")
resultado.pack(pady=5)

# Ejecutar la aplicación
ventana.mainloop()