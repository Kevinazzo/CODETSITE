from django.shortcuts import render
from products import models


def home(request):
    return render(request,'Productos.html')
