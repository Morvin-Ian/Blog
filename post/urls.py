from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='app-home'),
    path('blog/<str:pk>', views.blog, name='blog'),
  
]