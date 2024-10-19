from django.urls import path
from . import views

urlpatterns = [
    path("display", views.display, name="client-display"),
    path("counter", views.counter, name="client-counter"),
    path("register", views.register, name="client-register"),
    path("delete/<int:idR>", views.delete, name="client-delete"),
    path("update/<int:idR>", views.update, name="client-update"),
]
