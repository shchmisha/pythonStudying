from django.shortcuts import render
from django.core.urlresolvers import reverse_lazy
from django.views.generic import CreateView
# Create your views here.

from . import forms

class Signup(CreateView):
    form_class