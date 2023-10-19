from django.urls import path
from . import views

urlpatterns = [
    path("inicio/", views.mitemplate,name="inicio"),
    #path("'fecha/', otra vista"),
    #path('saludo/<str:nombre_completo>/', saludo)

]
