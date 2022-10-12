from pyexpat import model
import string
from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.utils import timezone
from . import models as db


# Create your views here.


# @register.filter
# def split(value):
#     list = value.split(" ")
#     return [list[0], list[1]]


class Home(TemplateView):
    template_name = "content/home.html"


class ContactUs(TemplateView):
    template_name = "content/contact.html"


class AboutUs(TemplateView):
    template_name = "content/about.html"


class Shop(ListView):
    model = db.products
    template_name = "content/shop.html"
    context_object_name = "products"
    # queryset = model.objects.all()
    # def get_context_data(self, **kwargs):
    #     images = db.images.objects.filter()
    #     context = super().get_context_data(**kwargs)
    #     context['products'] =
    #     return context


class Cart(TemplateView):
    template_name = "content/cart.html"


class WishList(TemplateView):
    template_name = "content/wishlist.html"


class CheckOut(TemplateView):
    template_name = 'content/checkout.html'


class viewProduct(DetailView):
    model = db.products
    template_name = "content/product_details.html"
    context_object_name = "items"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        product = self.get_object()
        context['images'] = db.images.objects.filter(products=product)
        return context
