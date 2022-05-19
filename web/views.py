from django.shortcuts import render
from django.http import  HttpResponse, HttpResponseRedirect
from .models import Flan, ContactForm
from .forms import ContactFormForm
from .forms import ContactFormModelForm
from django.contrib.auth.decorators import login_required

# Create your views here.
def indice(request):
    public_flans = Flan.objects.filter(is_private=False)
    
    return render(
        request,
        'index.html',
        {
            'public_flans':public_flans
        }
    )

def acerca(request):
    return render(request,'about.html',{})

@login_required
def bienvenido(request):
    private_flans = Flan.objects.filter(is_private=True)
    return render(
        request,
        'welcome.html',
        {
            'private_flans': private_flans
        }
    )

def contacto(request):
    if request.method == 'POST':
        #cree una instancia de formulario y rellénela con datos de la solicitud
        form = ContactFormModelForm(request.POST)
        if form.is_valid():
            #procesar los datos en form.cleaned_data según sea necesario
            #...
            contact_form = ContactForm.objects.create(**form.cleaned_data)
            # redirigir a nueva URL
            return HttpResponseRedirect('/exito')
    else:
        form = ContactFormModelForm()
    return render(request, 'contactus.html', {'form': form})

def exito(request):
    return render(request, 'success.html', {})


