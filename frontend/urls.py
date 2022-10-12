from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings
# from . import models

urlpatterns = [
    path("", views.Home.as_view(), name="home"),
    path("contact-us", views.ContactUs.as_view(), name="contact"),
    path("about-us", views.AboutUs.as_view(), name="aboutus"),
    path("shop", views.Shop.as_view(), name="shop"),
    path("cart", views.Cart.as_view(), name="cart"),
    path("wishlist", views.WishList.as_view(), name="wishlist"),
    path("checkout", views.CheckOut.as_view(), name="checkout"),
    path('item/<slug:slug>/',
         views.viewProduct.as_view(), name='product_details'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
