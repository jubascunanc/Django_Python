from django.shortcuts import render
from django.template import loader
from django.http import 

def crear_auto(request,marca, modelo,anio):
    
 auto = Auto(marca=marca, modelo=modelo, anio=anio,)   

auto.save()

template = loader.get_template('creacion_de_auto.html')
template_renderizado = template.render({crear_auto})