from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.


class Home(TemplateView):
    template_name = "content/home.html"


class ContactUs(TemplateView):
    template_name = "content/contact.html"


class AboutUs(TemplateView):
    template_name = "content/about.html"


class Shop(TemplateView):
    template_name = "content/shop.html"


class Cart(TemplateView):
    template_name = "content/cart.html"


class WishList(TemplateView):
    template_name = "content/wishlist.html"


class CheckOut(TemplateView):
    template_name = 'content/checkout.html'
