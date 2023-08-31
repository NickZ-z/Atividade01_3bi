from django.shortcuts import render, redirect, get_list_or_404, get_object_or_404
from .models import *
from .forms import *


def index(request): 
    if request.method == 'POST':
        form = ReservaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista')
    else:
        form = ReservaForm()
    
    return render(request,"index.html", {'form' : form})

def lista(request):
    reservas = Reserva.objects.all()

    return render(request,"lista.html", {'reserva' : reservas})

def detail(request,id):
    detail = get_object_or_404(Reserva,id=id)
    detalhes = Reserva.objects.all()

    return render(request, "detail.html",{'detalhes' : detalhes, 'detail' : detail})

def deletar_reserva(request, id):
    reserva = get_object_or_404(Reserva,id=id)
    reserva.delete()
    return redirect('lista')

    
