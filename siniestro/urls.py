from django.urls import path
from . import views

urlpatterns = [
    path("display", views.display, name="siniestro-display"),
    path("counter", views.counter, name="siniestro-counter"),
    path("register", views.register, name="siniestro-register"),
    path("delete/<int:idR>", views.delete, name="siniestro-delete"),
    path("update/<int:idR>", views.update, name="siniestro-update"),
]
