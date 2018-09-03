from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from django.views.generic import FormView
from .forms import JoinForm
from .mixins import AjaxFormMixin

class JoinFormView(AjaxFormMixin, FormView):
    form_class = JoinForm
    template_name = 'forms/ajax.html'
    success_url = '/form-success/'

    