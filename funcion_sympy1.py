# -*- coding: utf-8 -*-
"""
Created on Tue May  7 15:47:32 2019

@author: mquintana
"""

# importamos algunas funciones de la biblioteca math
from math import sin,cos,tan,asin,acos,atan,sqrt,log,exp, log1p
from math import sinh,cosh,tanh,asinh,acosh,atanh
from sympy.core.function import diff  # Para la derivada
from sympy.core.symbol import Symbol, S


x = Symbol('x') # nuestra var ind en las funciones
y = Symbol('y') # nuestra var dep en las funciones
#pedimos al usuario alguna función de una variable
#input produce dato de tipo str (una cadena de caracteres)
ec=input('De la funcion a resolver: ') #entra la ecuación

#Definimos una funcion f con un argumento x
exec ('ff = ' + ec)
exec ('f = lambda x: ' + ec)
derf = ff.diff(x)
exec ('df = lambda x: ' + str(derf))
print("f(x) = ",ff)
print("f'(x) = ",str(derf))
print("f({0}) = {1}".format(2.0,f(2.0)))
print("f'({0}) = {1}".format(2.0,df(2.0)))
