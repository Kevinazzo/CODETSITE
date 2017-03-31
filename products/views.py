from django.shortcuts import render
from products import models


def home(request):
    return render(request,'Productos.html')

def familyDetails(request, familia_id):
    return HttpResponse("<h1> Details for family "+str(familia_id)+"</h1>")