from django.shortcuts import render
from app.models import *
# Create your views here.
from django.views.generic import TemplateView,ListView,DetailView,CreateView

class Home(TemplateView):
    template_name='app/home.html'

class SchoolList(ListView):
    model = School
    context_object_name='schools'

class SchoolDetail(DetailView):
    model=School
    context_object_name='sclobject'

class SchoolCreate(CreateView):
    model=School
    fields='__all__'

