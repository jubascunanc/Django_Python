from django.shortcuts import render
from django.http import HttpResponse
from django.template  import loader
from .models import Auto
# Create your views here.

def mitemplate(request):
    
    milista = Auto.objects.all().values()

    template=loader.get_template("mi_template.html")

    context={
        "milista": milista,
    }

    return HttpResponse(template.render(context,request))

