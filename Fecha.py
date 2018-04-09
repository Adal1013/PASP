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

    def validarBisiesto(self):
        if self.year%4==0 and (self.year%100!=0 or self.year%400==0):
            return True
        else:
            return False

    def validarFecha(self):
        if self.mes < 1 or self.mes > 12:
            return ("Fecha invalida")
        else:
            if self.validarBisiesto():
                if self.mes == 2:
                    if self.dia>29:
                        return ("Fecha invalida")
                else:
                    if self.dia > self.numDiasxmes[self.mes]:
                        return ("Fecha invalida") 
            else:    
                if self.dia > self.numDiasxmes[self.mes]:
                    return ("Fecha invalida")
        return ("Fecha valida")         

    def formatoLatino(self):
        return self.dia + "/" + self.mes + "/" + self.year


    def formatoGringo(self):
        print("("+mes+"/"+year+"/"+year+")")

        


