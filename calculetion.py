from tkinter import *

#Constantes
ventana = Tk()
ventana.title("Calculadora")
i = 0

#Entry windowns
e_text = Entry(ventana, font=("Calibri 20"))
e_text.grid(row = 0, column = 0, columnspan = 4, padx = 5, pady = 5)

#funciones
def click_boton(valor):
    global i
    e_text.insert(i, valor)
    i += 1
    return

def delete_cal():
    global i
    i = 0
    e_text.delete(0, END)

def resul():
    ecuation = e_text.get()
    res = eval(ecuation)
    e_text.delete(0, END)
    e_text.insert(0,res)

#Buttons - numer
button_1 = Button(ventana,text = "1", width = 5, height = 2, command = lambda:click_boton(1))
button_2 = Button(ventana,text = "2", width = 5, height = 2, command = lambda:click_boton(2))
button_3 = Button(ventana,text = "3", width = 5, height = 2, command = lambda:click_boton(3))
button_4 = Button(ventana,text = "4", width = 5, height = 2, command = lambda:click_boton(4))
button_5 = Button(ventana,text = "5", width = 5, height = 2, command = lambda:click_boton(5))
button_6 = Button(ventana,text = "6", width = 5, height = 2, command = lambda:click_boton(6))
button_7 = Button(ventana,text = "7", width = 5, height = 2, command = lambda:click_boton(7))
button_8 = Button(ventana,text = "8", width = 5, height = 2, command = lambda:click_boton(8))
button_9 = Button(ventana,text = "9", width = 5, height = 2, command = lambda:click_boton(9))
button_0 = Button(ventana,text = "0", width = 15, height = 2, command = lambda:click_boton(0))

#Buttons - function
button_ac = Button(ventana,text = "AC", width = 5, height = 2, command = lambda:delete_cal())
button_parentesis1 = Button(ventana,text = "(", width = 5, height = 2, command = lambda:click_boton("("))
button_parentesis2 = Button(ventana,text = ")", width = 5, height = 2, command = lambda:click_boton(")"))
button_punto = Button(ventana,text = ".", width = 5, height = 2, command = lambda:click_boton("."))

#Buttons - operaction
button_div = Button(ventana,text = "/", width = 5, height = 2, command = lambda:click_boton("/"))
button_mult = Button(ventana,text = "x", width = 5, height = 2, command = lambda:click_boton("x"))
button_sum = Button(ventana,text = "+", width = 5, height = 2, command = lambda:click_boton("+"))
button_rest = Button(ventana,text = "-", width = 5, height = 2, command = lambda:click_boton("-"))
button_igual = Button(ventana,text = "=", width = 5, height = 2, command = lambda:resul())


#agregar buttons
button_ac.grid(row = 1, column = 0, padx = 5, pady = 5)
button_parentesis1.grid(row = 1, column = 1, padx = 5, pady = 5)
button_parentesis2.grid(row = 1, column = 2, padx = 5, pady = 5)
button_div.grid(row = 1, column = 3, padx = 5, pady = 5)

button_7.grid(row = 2, column = 0, padx = 5, pady = 5)
button_8.grid(row = 2, column = 1, padx = 5, pady = 5)
button_9.grid(row = 2, column = 2, padx = 5, pady = 5)
button_mult.grid(row = 2, column = 3, padx = 5, pady = 5)

button_4.grid(row = 3, column = 0, padx = 5, pady = 5)
button_5.grid(row = 3, column = 1, padx = 5, pady = 5)
button_6.grid(row = 3, column = 2, padx = 5, pady = 5)
button_sum.grid(row = 3, column = 3, padx = 5, pady = 5)

button_1.grid(row = 4, column = 0, padx = 5, pady = 5)
button_2.grid(row = 4, column = 1, padx = 5, pady = 5)
button_3.grid(row = 4, column = 2, padx = 5, pady = 5)
button_rest.grid(row = 4, column = 3, padx = 5, pady = 5)

button_0.grid(row = 5, column = 0, columnspan = 2,padx = 5, pady = 5)
button_punto.grid(row = 5, column = 2, padx = 5, pady = 5)
button_igual.grid(row = 5, column = 3, padx = 5, pady = 5)


ventana.mainloop()
