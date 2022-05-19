from django.shortcuts import render
from .models import Flan
# Create your views here.
def indice(request):
    public_flans=Flan.objects.filter(is_private=False)
    
    return render(
        request,
        'index.html',
        {
        'public_flans':public_flans
        }
    )

def acerca(request):
    return render(request,'about.html',{})

def bienvenido(request):
    private_flans =Flan.objects.filter(is_private=True)
    return render(
        request,'welcome.html',{
            'private_flans': private_flans
        }
    )

