"""django_boilerplate URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path,include
from app.views import home
from django.conf.urls.static import static  
from django.conf import settings
from django.shortcuts import redirect

import os

def redirecting(request):
    return redirect(f"{os.getenv('BASE_URL')}/")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',redirecting,name='redirecting'),
    path(f'{os.getenv("BASE_URL")}/',include([
        path('',home,name='home'),
        # """
        # Include your others paths here like
        # 1.) path('some_route/', views.home, name='home')
        # 2.) path('some_route/', Home.as_view(), name='home') for class based views
        # 3.) path('some_route/', include('your_app_name.urls'))
        # """
    ]))
]

urlpatterns+=static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
