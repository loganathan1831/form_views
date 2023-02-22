from django.shortcuts import render
from django.views.generic import FormView
from app.forms import *
from django.http import HttpResponse
# Create your views here.


#this is djangoforms base views
class Student_form_data(FormView):
    template_name='Student_from_data.html'
    form_class=StudentForm

    def form_valid(self, form):
        data=form.cleaned_data
        return HttpResponse(str(data))

#this is for modelbase views

class studentlist(FormView):
    template_name='studentlist.html'
    form_class=student_listForm

    def form_valid(self, form):
        form.save()
        return HttpResponse('student list is done successfully')