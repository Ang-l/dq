from django.urls import path,include
from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework import routers
from django.conf.urls.static import static
from django.conf import settings
from user import views


router = routers.DefaultRouter()
router.register(r'user', views.UserView)

urlpatterns=[
    path('', include(router.urls)),
]