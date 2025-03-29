from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('about/', views.about),
    path('booking/', views.booking),
    path('login/', views.login),
    path('signup/', views.signup),
    path('menu/', views.menu),
    path('logout/', views.logout),
]
