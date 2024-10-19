from django.urls import path
from . import views

urlpatterns = [
    path("display", views.display, name="poliza-display"),
    path("counter", views.counter, name="poliza-counter"),
    path("register", views.register, name="poliza-register"),
    path("delete/<int:idR>", views.delete, name="poliza-delete"),
    path("update/<int:idR>", views.update, name="poliza-update"),
]
