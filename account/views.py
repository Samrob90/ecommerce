from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.


class Account(TemplateView):
    template_name = "content/account/index.html"
