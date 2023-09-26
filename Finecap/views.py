from django.shortcuts import render, redirect, get_list_or_404, get_object_or_404
from .models import *
from .forms import *
import datetime
from .filters import ReservaFilter
from django_filters.views import FilterView

def index(request): 
    data_atual = datetime.datetime.now()
    if request.method == 'POST':
        form = ReservaForm(request.POST)
        if form.is_valid():
            reserva = form.save(commit=False)
            reserva.data_reserva = data_atual
            reserva.save()
            return redirect('lista')
    else:
        form = ReservaForm()
    
    return render(request,"index.html", {'form' : form})

def lista(request):
    reservas = Reserva.objects.all().order_by('data_reserva')
    f = ReservaFilter(request.GET, queryset=Reserva.objects.all())
    return render(request,"lista.html", {'reserva' : reservas, 'filter':f})

def detail(request,id):
    detail = get_object_or_404(Reserva,id=id)
    detalhes = Reserva.objects.all()

    return render(request, "detail.html",{'detalhes' : detalhes, 'detail' : detail})

def deletar_reserva(request, id):
    reserva = get_object_or_404(Reserva,id=id)
    reserva.delete()
    return redirect('lista')


