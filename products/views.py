from django.shortcuts import render
from products import models


def home(request, families):
    families = [
        ('Tornillo',models.Familia.objects.filter(nombre="Tornillo")),
        ('Tuerca',models.Familia.objects.filter(nombre="Tuerca")),
    ]
    context = [
        ("Tornillos", models.Subtipo.objects.filter(familia_ID=families['Tornillo'])),
    ]
    return render(request,'Productos.html',context)
