from django.urls import path
from . import views

urlpatterns = [
    path("display", views.display, name="reclamo-display"),
    path("counter", views.counter, name="reclamo-counter"),
    path("register", views.register, name="reclamo-register"),
    path("delete/<int:idR>", views.delete, name="reclamo-delete"),
    path("update/<int:idR>", views.update, name="reclamo-update"),
]
