from django.urls import path,include
from app01 import views

urlpatterns=[
    path('index/',views.index_view)
]