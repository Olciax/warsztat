from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .models import *
from django.urls import reverse_lazy


def view(request):
    person = Person.objects.order_by('surname')
    ctx = {
        'person': person,

    }
    return render(request, 'mail/index.html', ctx)


def details(request, person_id):
    # person = Person.objects.get(pk=person_id)
    person = get_object_or_404(Person, pk=person_id)
    tel = Telephone.objects.filter(person=person)
    # adr = Address.objects.filter(person=person)
    mail = Email.objects.filter(person=person)
    ctx = {
        'person': person,
        'tel': tel,
        'mail': mail,
    }
    return render(request, 'mail/details.html', ctx)



class PersonCreate(CreateView):
    model = Person
    fields = ['name', 'surname', 'description']

class PersonUpdate(UpdateView):
    model = Person
    fields = ['name', 'surname', 'description']

class Address(UpdateView):
    model = Address
    fields = ['street']


class PersonDelete(DeleteView):
    model = Person
    success_url = reverse_lazy('index')
# Create your views here.
