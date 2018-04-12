#!/usr/bin/python
#-*- coding: utf-8 -*-

from Fecha import Fecha

class Prestamo:
    def __init__(self,numPrestamo,valor,fechaAutorizacion,fechaEntrega,Solicitante):
        self.numPrestamo = numPrestamo
        self.valor = valor
        self.fechaAutorizacion = fechaAutorizacion
        self.fechaEntrega = fechaEntrega
        self.datosSolicitante = []
        self.capturarDatos(Solicitante)

    def capturarDatos(self, Solicitant):
        self.datosSolicitante.append(Solicitant)
