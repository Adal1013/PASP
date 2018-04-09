#!/usr/bin/python
#-*- coding: utf-8 -*-

from Fecha import Fecha
from Prestamo import Prestamo
from Persona import Persona

fecha1 = Fecha()
fecha1.getDate()
print(fecha1.getDay())
print(fecha1.getMonth())
print(fecha1.getYear())
print(fecha1.validarFecha())
print(fecha1.formatoLatino())
fecha1.formatoGringo()