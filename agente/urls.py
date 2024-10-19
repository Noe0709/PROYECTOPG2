from django.urls import path
from . import views

urlpatterns = [
    path("display", views.display, name="agente-display"),
    path("counter", views.counter, name="agente-counter"),
    path("register", views.register, name="agente-register"),
    path("delete/<int:idR>", views.delete, name="agente-delete"),
    path("update/<int:idR>", views.update, name="agente-update"),
]
