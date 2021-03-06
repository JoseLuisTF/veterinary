"""Veterinary URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from Veterinary.views import HomeView
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required
from apps.usuario.views import signup_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('usuario/', include('apps.usuario.urls')),
    path('mascota/', include('apps.mascota.urls')),
    path('cita/', include('apps.cita.urls')),
    path('', login_required(HomeView.as_view()), name='home'),
    path('accounts/login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(template_name='logout.html'), name='logout'),
    path('accounts/signup/', signup_view, name='signup'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

