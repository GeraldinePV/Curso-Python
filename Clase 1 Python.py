# -*- coding: utf-8 -*-
"""
Created on Sat May 22 09:36:59 2021

@author: USER
"""
#programa para calcular el salario

nombre = input('Ingrese su nombre: ')
apellido = input(f'{nombre}, ingrese sus apellidos: ')
edad = input(f'{nombre}, ingrese su edad: ')
h = int(input(f'{nombre}, ingrese el numero de horas laboradas por semana: '))
p = float(input(f'{nombre}, ingrese el precio de la hora '
                '(sin puntos, ni comas, solo el número): '))
sueldo = (h * p)
total =  (sueldo - 0.1)

pago = print('Hola,', nombre, apellido,
             'su pago en la semana es ${:.1f}'.format(total))

