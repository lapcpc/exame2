from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import View
from .forms import RegistroForm
from .models import Registro
import datetime
from django.contrib import messages
# Create your views here.


class Home(View):
    def get(self,request):
        registroo = Registro.objects.all()
        form = RegistroForm()
        context = {'form': form,
                    'registroo': registroo}
        return render(request, 'index.html', context)

    def post(self, request):
            form = RegistroForm(request.POST)
            if form.is_valid():
                entrada = form.save(commit=False)
                entrada.save()
                return redirect('index')
            else:
                context = {'form': form}
                return render(request, 'index.html', context)