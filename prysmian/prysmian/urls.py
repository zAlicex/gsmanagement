from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect
from django.contrib.auth import views as auth_views
from django.shortcuts import render
from . import views



urlpatterns = [
    path('admin/', admin.site.urls),
    path('registros/', include('registros.urls')),
    path('', views.home, name='home'),
    path('sed/', include('sed.urls')),
    path('login/', auth_views.LoginView.as_view(
        template_name='login.html', 
        next_page='home',
        redirect_authenticated_user=True
    ), name='login'),
    path('logout/', views.custom_logout, name='logout'),
    path('test-auth/', views.test_auth, name='test_auth'),
]
