from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("product/<int:id>", views.product_detail, name="product_detail"),
]
