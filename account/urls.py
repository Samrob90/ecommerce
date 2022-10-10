from unicodedata import name
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", views.Account.as_view(), name='account'),
    path("upload", views.addItem, name="upload")

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
