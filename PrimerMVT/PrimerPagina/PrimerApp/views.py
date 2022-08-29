
from tkinter import N
from django.shortcuts import render
from PrimerApp.models import Familia, Nico, Flor, Paco
from django.http import HttpResponse

# Create your views here.
def estaFamilia(self):
    
    estaFamilia = Familia(nombre="Citrus")
    estaFamilia.save()
    documentoDeTexto = f"--->Familia: {estaFamilia.nombre}"
    return HttpResponse(documentoDeTexto)

def elLimon(self):
    
    elLimon = Nico(nombre="Nicolás", apellido="Limón", fecha_nacimiento="1995-09-29")
    elLimon.save()
    documentoDeTexto1 = f"--->Nombre: {elLimon.nombre}     Apellido: {elLimon.apellido}     Edad: {elLimon.edad}     Fecha de nacimiento: {elLimon.fecha_nacimiento}"
    return HttpResponse(documentoDeTexto1)

def laLimita(self):
    
    laLimita = Flor(nombre="Florencia", apellido="Lima", fecha_nacimiento="1998-02-22")
    laLimita.save()
    documentoDeTexto2 = f"--->Nombre: {laLimita.nombre}     Apellido: {laLimita.apellido}     Edad: {laLimita.edad}    Fecha de nacimiento: {laLimita.fecha_nacimiento}"
    return HttpResponse(documentoDeTexto2)

def elPato(self):
    
    elPato = Paco(nombre="Paco el Pato", fecha_nacimiento="2022-07-22")
    elPato.save()
    documentoDeTexto3 = f"--->Nombre: {elPato.nombre}     Fecha de nacimiento: {elPato.fecha_nacimiento}"
    return HttpResponse(documentoDeTexto3)