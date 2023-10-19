from django.shortcuts import render
from django.template import load
from django.http import django

def crear_auto(request,marca, modelo,anio):
    
 auto = crear_auto(marca=marca, modelo=modelo, anio=anio,)   

crear_auto.save()

template = load.get_template('creacion_de_auto.html')
template_renderizado = template.render({crear_auto})