from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.edit import FormView

from applications import departamento
from .forms import NewDepartamentoForm

from applications.persona.models import Empleado
from .models import Departamento
# Create your views here.



class DepartamentoListView(ListView):
    model = Departamento
    template_name = "departamento/lista.html"
    context_object_name = 'departamentos'


class NewDepartamnetoView(FormView):
    template_name = 'departamento/new_departamento.html'
    form_class = NewDepartamentoForm
    success_url = '/'

    def form_valid(self, form):
        print('*********estamos en el forms valid')

        depa = Departamento(
            name=form.cleaned_data['departamento'],
            shor_name=form.cleaned_data['shorname'],

        )
        depa.save()

        nombre = form.cleaned_data['nombre']
        apellido = form.cleaned_data['apellidos']
        Empleado.objects.create(
            first_name=nombre,
            last_name=apellido,
            job='1',
            departamento=depa
        )
        
        return super(NewDepartamnetoView, self).form_valid(form)
    




