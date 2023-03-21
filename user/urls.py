from django.urls import path
from . import views

urlpatterns = [
    path('', views.homePage, name='home'),
    path('user-profile/', views.userProfile, name='user-profile'),
    path('sign-up/', views.registerPage, name='sign-up'),
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutPage, name='logout'),
]