from django.urls import path
from . import views

urlpatterns = [
    path("display", views.display, name="user-display"),
    path("register", views.register, name="user-egister"),
    path("update/<int:user_id>", views.update, name="user-update"),
    path("delete/<int:user_id>", views.delete, name="user-delete"),
]
