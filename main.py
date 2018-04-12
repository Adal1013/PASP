#!/usr/bin/python
#-*- coding: utf-8 -*-

from Fecha import Fecha
from Prestamo import Prestamo
from Persona import Persona

fecha1 = Fecha()
fecha1.getDate()
print(fecha1.validarFecha())
print(fecha1.formatoLatino())
print(fecha1.formatoGringo())
fecha2 = Fecha()
fecha2.getDate()
print(fecha1.validarFecha())
#solic = Solicitante(1,"Jose","Cuervo","425400","3002001000")
solic = Persona(1,"Jose","Cuervo","425400","3002001000")
pres = Prestamo(1,25000,fecha1,fecha2)
pres.capturarDatos(solic)