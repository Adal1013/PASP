#!/usr/bin/python
#-*- coding: utf-8 -*-

from Persona import Persona

class Asesor(Persona):
    def __init__(self,id,firstname,lastname,homephone,celphone,username):
    	Persona.__init__(self,id,firstname,lastname,homephone,celphone)
        self.username = username

