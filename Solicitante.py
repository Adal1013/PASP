#!/usr/bin/python
#-*- coding: utf-8 -*-

from Persona import Persona

class Solicitante(Persona):
	def __init__(self,id,firstname,lastname,homephone,celphone):
		Persona.__init__(self,id,firstname,lastname,homephone,celphone)