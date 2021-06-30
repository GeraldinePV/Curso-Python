#Calculadora 
#Inicio 26/06/21 - Fin 29/06/21 
from tkinter import *
from tkinter import messagebox

#ventana
ventana = Tk()
ventana.title('Calculadora')
ventana.geometry("274x328")
ventana.resizable(0,0)
ventana.config(bg = 'white')

#efecto color

class HoverButton(Button):
  def __init__(self, master, **kw):
      Button.__init__(self, master=master, **kw)
      self.defaulBackground = self['background']
      self.bind("<Enter>", self.on_enter)
      self.bind("<Leave>", self.on_leave)

  def on_enter(self, e):
    self['background'] = self['activebackground']

  def on_leave(self, e):
    self['background'] = self.defaulBackground

#obtener dato
i = 0
def obtener_dato(dato):
  global i
  i += 1
  entradas.insert(i, dato)

#operaciones
def operaciones():
  global i
  ecuacion = entradas.get()
  if i != 0:
    try:
      result = str(eval(ecuacion))
      entradas.delete(0,END)
      entradas.insert(0,result)
      longitud = len(result)
      i = longitud
    
    except:
      result = 'ERROR'
      entradas.delete(0,END)
      entradas.insert(0,result)
  else:
    pass

#funciones borrar
def borrar_uno():
	global i 
	if i==-1:
		pass
	else:
		entradas.delete(i,last =None)
		i-=1

def borrar_todo():
	entradas.delete(0, END)	
	i=0

frame = Frame(ventana, bg ='black', relief = "raised")
frame.grid(column = 0, row = 0, padx = 6, pady = 3)

entradas = Entry(frame,bg='#9EF8E8', width = 21, relief='groove', font = 'Montserrat 16',justif = 'right')
entradas.grid(columnspan = 4 , row = 0, pady = 3, padx = 1, ipadx = 1, ipady = 1) 


# Botones
#Fila 1

Boton1 = HoverButton(frame, text = '1', bg = '#9a33de', borderwidth=2, height=2, width=5, font= ('Comic sens MC',12,'bold'),
relief = "raised", activebackground="aqua",  anchor="center", command=lambda: obtener_dato(1))
Boton1.grid(column = 0 ,row = 1, pady = 1, padx = 3)

Boton2 = HoverButton(frame, text = '2', bg = '#9a33de', borderwidth=2, height=2, width=5, font= ('Comic sens MC',12,'bold'),
relief = "raised", activebackground="aqua",  anchor="center", command=lambda: obtener_dato(2))
Boton2.grid(column = 1, row = 1, pady = 1, padx = 1)

Boton3 = HoverButton(frame, text = '3', bg = '#9a33de', borderwidth=2, height=2, width=5, font= ('Comic sens MC',12,'bold'),
relief = "raised", activebackground="aqua",  anchor="center", command=lambda: obtener_dato(3))
Boton3.grid(column = 2, row = 1, pady = 1, padx = 1)

Boton_borrar = HoverButton(frame, text= "⌫", height=2, width=5,font= ('Comic sens MC',12,'bold'), 
borderwidth=2,  relief = "raised", activebackground="#ffbf00", bg='#ff9900',  anchor="center",command=lambda: borrar_uno())  
Boton_borrar.grid(column =3, row=1, pady=2,padx=2)

#Fila 2

Boton4 = HoverButton(frame, text = '4', bg = '#9a33de', borderwidth = 2, height = 2, width = 5, font = ('Comic sens MC',12,'bold'), 
relief = "raised", activebackground ="aqua",  anchor = "center", command = lambda: obtener_dato(4))
Boton4.grid(column = 0, row = 2, pady = 1, padx = 3)

Boton5 = HoverButton(frame, text = '5', bg = '#9a33de', borderwidth = 2, height = 2, width = 5, font = ('Comic sens MC',12,'bold'),
relief = "raised", activebackground = 'aqua', anchor = "center", command = lambda: obtener_dato(5))
Boton5.grid(column = 1, row = 2, pady = 1, padx = 1)

Boton6 = HoverButton(frame, text = '6', bg = '#9a33de', borderwidth = 2, height = 2, width = 5, font = ('Comic sens MC',12,'bold'),
relief = 'raised', activebackground = 'aqua', anchor = 'center', command = lambda: obtener_dato(6))
Boton6.grid(column = 2, row = 2, pady = 1, padx = 1)

Boton_mas = HoverButton(frame, text = '+', bg = '#00a2ff', borderwidth = 2, height = 2, width = 5, font = ('Comic sens MC',12,'bold'), 
relief = "raised", activebackground ="#22ff00",  anchor = "center", command = lambda: obtener_dato('+'))
Boton_mas.grid(column = 3, row = 2, pady = 1, padx = 3)

#Fila 3

Boton7 = HoverButton(frame, text = '7', bg = '#9a33de', borderwidth = 2, height = 2, width = 5, font = ('Comic sens MC',12,'bold'),
relief = 'raised', activebackground = 'aqua', anchor = 'center', command = lambda: obtener_dato(7))
Boton7.grid(column = 0, row = 3, pady = 1, padx = 3)

Boton8 = HoverButton(frame, text = '8', bg = '#9a33de', borderwidth = 2, height = 2, width = 5, font = ('Comic sens MC',12,'bold'),
relief = 'raised', activebackground = 'aqua', anchor = 'center', command = lambda: obtener_dato(8))
Boton8.grid(column = 1, row = 3, pady = 1, padx = 1)

Boton9 = HoverButton(frame, text = '9', bg = '#9a33de', borderwidth = 2, height = 2, width = 5, font = ('Comic sens MC',12,'bold'),
relief = 'raised', activebackground = 'aqua', anchor = 'center', command = lambda: obtener_dato(9))
Boton9.grid(column =2, row = 3, pady = 1, padx = 1)

Boton_menos = HoverButton(frame, text = '-', bg = '#00a2ff', borderwidth = 2, height = 2, width = 5, font = ('Comic sens MC',12,'bold'), 
relief = "raised", activebackground ="#22ff00",  anchor = "center", command = lambda: obtener_dato('-'))
Boton_menos.grid(column = 3, row = 3, pady = 1, padx = 3)

#Fila 4

Boton0 = HoverButton(frame, text = '0', bg = '#9a33de', borderwidth = 2, height = 5, width = 5, font = ('Comic sens MC',12,'bold'),
relief = 'raised', activebackground = 'aqua', anchor = 'center', command = lambda: obtener_dato(0))
Boton0.grid(column =0, rowspan = 2, row = 4, pady = 1, padx = 1)

Boton_punto = HoverButton(frame, text= ".", height=2, width=5,font= ('Comic sens MC',12,'bold'), borderwidth=2, 
relief = "raised", activebackground="aqua", bg ='#9a33de', anchor="center",command=lambda: obtener_dato('.'))  
Boton_punto.grid(column =1 , row=4, pady=1,padx=1)

Boton_division = HoverButton(frame, text = '÷', bg = '#00a2ff', borderwidth = 2, height = 2, width = 5, font = ('Comic sens MC',12,'bold'), 
relief = "raised", activebackground ="#22ff00",  anchor = "center", command = lambda: obtener_dato('/'))
Boton_division.grid(column = 2, row = 4, pady = 1, padx = 3)

Boton_por = HoverButton(frame, text = 'x', bg = '#00a2ff', borderwidth = 2, height = 2, width = 5, font = ('Comic sens MC',12,'bold'), 
relief = "raised", activebackground ="#22ff00",  anchor = "center", command = lambda: obtener_dato('*'))
Boton_por.grid(column = 3, row = 4, pady = 1, padx = 3)

#Fila 5

Button_igual = HoverButton(frame, text= "=", height=2, width=12,font= ('Comic sens MC',12,'bold'), borderwidth=2, 
relief = "raised", activebackground="#07faad", bg='#15c238', anchor="center",command=lambda: operaciones())  
Button_igual.grid(column =1 ,columnspan=2, row=5, pady=1,padx=1)


Button_borrar = HoverButton(frame, text= "C", height=2, width=5,font= ('Comic sens MC',12,'bold'), borderwidth=2, 
relief = "raised", activebackground="#eaff00", bg='#ffa200', anchor="center",command=lambda: borrar_todo())  
Button_borrar.grid(column =3, row=5, pady=2,padx=2)

ventana.mainloop()

