"""Lab3 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path
from userauth import views

urlpatterns = [
    path('login/', views.login_view, name='login'),
<<<<<<< HEAD
    path('success/', views.success_page, name='success_page'),
=======
    path('success_page/', views.success_page, name='success'),
>>>>>>> refs/remotes/origin/master
    # Add more URL patterns as needed
]
