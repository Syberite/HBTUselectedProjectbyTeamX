"""
URL configuration for HBTUWEBSITE project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path
from home import views 

admin.site.site_header = "R&D lab Admin"
admin.site.site_title = "LabAdminPortal"
admin.site.index_title = "Welcome to lab admin Portal"


urlpatterns = [
    path('', views.index, name='home'),
    path("Login", views.Login, name="Login"),
    path("services", views.services , name='services'),
    path("contact", views.contact, name="contact"),
    path('admin/', admin.site.urls),
    path('AiProject', views.AiProject ,name="AiProject"),
    path('DLproject', views.DLproject , name="DLproject"),
    path('Webdev', views.Webdev , name="Webdev"),
    path('Login2', views.Login2, name='Login2'),
]
