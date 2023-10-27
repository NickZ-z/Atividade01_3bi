from django.shortcuts import render, redirect, get_list_or_404, get_object_or_404
from .models import *
from .forms import *
import datetime
from .filters import ReservaFilter
from django_filters.views import FilterView
from django.contrib.auth import authenticate, login, logout
from .forms import LoginForm, UserForm
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator

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
    
    return render(request,"add.html", {'form' : form})


def lista(request):
    reservas = Reserva.objects.all().order_by('data_reserva')
    f = ReservaFilter(request.GET, queryset=Reserva.objects.all())
   
    pagina = request.GET.get('page')
    paginator = Paginator(f.qs, 5)
    pag_obj = paginator.page(paginator.num_pages)
    return render(request,"lista.html", {'reserva' : pag_obj, 'filter':f})
def detail(request,id):
    detail = get_object_or_404(Reserva,id=id)
    detalhes = Reserva.objects.all()

    return render(request, "detail.html",{'detalhes' : detalhes, 'detail' : detail})

def deletar_reserva(request, id):
    reserva = get_object_or_404(Reserva,id=id)
    reserva.delete()
    return redirect('lista')


def create_user(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.is_active = True
            user.is_staff = True
            user.save()
            return redirect('login')

    else:
        form = UserForm()

    context = {'form': form}
    return render(request, 'create_user.html', context)

def login_view(request):
    if request.method == 'POST':
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            user = authenticate(username=login_form.cleaned_data['username'],
                                password=login_form.cleaned_data['password'])
            print(user)
            if user is not None:
                login(request, user)
                return redirect('index')


    else:
        login_form = LoginForm()

    context = {'login_form': login_form}
    return render(request, 'login.html', context)

def logout_view(request):
    logout(request)
    return redirect('login')