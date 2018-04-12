#!/usr/bin/python
#-*- coding: utf-8 -*-

from Fecha import Fecha

class Prestamo:
    def __init__(self,numPrestamo,valor,fechaAutorizacion,fechaEntrega):
        self.numPrestamo = numPrestamo
        self.valor = valor
        self.fechaAutorizacion = fechaAutorizacion
        self.fechaEntrega = fechaEntrega
        self.datosSolicitante = []

    def capturarDatos(self, Solicitante):
        self.datosSolicitante.append(Solicitante)

    def sumSevenDays(self):
        aux=self.fechaAutorizacion.dia+7

