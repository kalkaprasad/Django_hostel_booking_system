"""kp1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from .views import index
from .views import contact
from .views import hostels
from .views import about
from .views import signup
from .views import login
from .views import emp
from .views import show
from .views import success
from .views import hostelfound
from .views import userpage
from django.conf.urls import url,include
from .views import upload
from .views import fetchhostel
from .views import AdminLogin
from .views import logout
from .views import dashboard
from .views import searchhostel
from .views import camera
urlpatterns = [
    path('myvalue', admin.site.urls),
    path('',index,),
    path('hostel',hostels,name="hostels"),
    path('contact',contact,name="contact"),
    path('about',about),
    path('signup',signup,name="signup"),
    path('login',login,name="login"),
    path('emp',emp,name="emp"),
    path('show',show,name="show"),
    path('success/',success,name="success"),
    path('hostelfound',hostelfound,name="hostelfound"),
    path('userpage',userpage,name="userpage"),
    path('upload',upload,name="upload"),
    path('fetch',fetchhostel,name="fetch"),
    path("mylogin.go",AdminLogin,name="mylogin.go"),
    path("logout",logout,name="logout"),
    path("dashboard",dashboard,name="dashboard"),
    path('searchhostel',searchhostel,name='searchhostel'),
    path('camera',camera,name="camera"),
]
