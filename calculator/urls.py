"""
URL configuration for calculator project.

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
from operations.views import AdditionView,SubstractionView,MultiplicationView,FactView,PrimeNumberView
#localhost:8000/add/
#localhost:8000/substract/
#localhost:8000/multiplicate/
#localhost:8000/fact/
#localhost:8000/prime/

urlpatterns = [
    path('admin/', admin.site.urls),
    path("add/",AdditionView.as_view()),
    path("substract/",SubstractionView.as_view()),
    path("multiplicate/",MultiplicationView.as_view()),
    path("fact/",FactView.as_view()),
    path("prime/",PrimeNumberView.as_view())
]
