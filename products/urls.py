from django.urls import path
from . import views

urlpatterns = [
    path("display", views.display, name="product-display"),
    path("counter", views.counter, name="product-counter"),
    path("register", views.register, name="product-register"),
    path("delete/<int:idR>", views.delete, name="product-delete"),
    path("update/<int:idR>", views.update, name="product-update"),
]
