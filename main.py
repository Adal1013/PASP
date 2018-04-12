#!/usr/bin/python
#-*- coding: utf-8 -*-

from Solicitante import Solicitante
from Fecha import Fecha
from Prestamo import Prestamo
from Persona import Persona

f1 = Fecha()
f1.getDate()
while f1.validarFecha() != True:
	print("Fecha invalida, por favor ingresa una fecha valida")
	f1.getDate()
print("Fecha Valida")
print(f1.formatoLatino())
print(f1.formatoGringo())
f2 = Fecha()
f2.sumSevenDays(f1)
if f2.validarFecha(): print("Fecha Valida")
print(f2.formatoLatino())
print(f2.formatoGringo())
solic = Solicitante(1,"Jose","Cuervo","425400","3002001000")
pres = Prestamo(1,25000,f1,f2,solic)
