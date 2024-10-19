from django.urls import path
from . import views

urlpatterns = [
    path("display", views.display, name="indicador-display"),
    path("counter", views.counter, name="indicador-counter"),
    path("register", views.register, name="indicador-register"),
    path("delete/<int:idR>", views.delete, name="indicador-delete"),
    path("update/<int:idR>", views.update, name="indicador-update"),
]
