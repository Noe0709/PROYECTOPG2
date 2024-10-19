from django.urls import path

from . import views

urlpatterns = [
    path('', views.login_view, name='login'),
    path('register', views.authLogin, name='register'),
    path('auth', views.authLogin, name='auth'),
     path('logout', views.logout_view, name='logout'),
]