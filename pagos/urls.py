from django.urls import path
from . import views

urlpatterns = [
    path("display", views.display, name="pago-display"),
    path("counter", views.counter, name="pago-counter"),
    path("register", views.register, name="pago-register"),
    path("delete/<int:idR>", views.delete, name="pago-delete"),
    path("update/<int:idR>", views.update, name="pago-update"),
]
