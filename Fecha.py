#!/usr/bin/python
#-*- coding: utf-8 -*-

class Fecha:

    numDiasxmes = {1:31, 2:28, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}

    def __init__(self):
        self.dia = None
        self.mes = None 
        self.year = None

    def getDate(self):
        self.dia=int(input("Ingrese el dia: "))
        self.mes=int(input("Ingrese el mes: "))
        self.year=int(input("Ingrese el año: "))
        
    def getDay(self):
        return self.dia

    def getMonth(self):
        return self.mes

    def getYear(self):
        return self.year       

    def formatoLatino(self):
        return "Formato Latino: (" + str(self.dia) + "/" + str(self.mes) + "/" + str(self.year) + ")"

    def formatoGringo(self):
        return "Formato Gringo: (" + str(self.mes) + "/" + str(self.dia) + "/" + str(self.year) + ")"

    def validarBisiesto(self):
        if self.year%4==0 and (self.year%100!=0 or self.year%400==0):
            return True
        else:
            return False

    def validarFecha(self):
        if self.year > 2100:
            return False            
        else:
            if self.mes < 1 or self.mes > 12:
                return False
            else:
                if self.validarBisiesto():
                    if self.mes == 2:
                        if self.dia>29:
                            return False
                    else:
                        if self.dia > self.numDiasxmes[self.mes]:
                            return False 
                else:    
                    if self.dia > self.numDiasxmes[self.mes]:
                        return False
        return True  

    def sumSevenDays(self, fechaAutorizacion):
        auxDia = fechaAutorizacion.dia + 7
        auxMes = fechaAutorizacion.mes
        auxYear = fechaAutorizacion.year
        if auxDia > self.numDiasxmes[fechaAutorizacion.mes]:
            auxMes = fechaAutorizacion.mes + 1
            if auxMes > 12:
                auxMes = 1
                auxYear = fechaAutorizacion.year + 1
            auxDia = auxDia - self.numDiasxmes[fechaAutorizacion.mes]
        self.dia=auxDia
        self.mes=auxMes
        self.year=auxYear


        

        


