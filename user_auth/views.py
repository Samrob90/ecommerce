from django.shortcuts import render
from django.views.generic import TemplateView


# Create your views here.

class Login(TemplateView):
    template_name = "content/authentication/login.html"


class Register(TemplateView):
    template_name = "content/authentication/register.html"
