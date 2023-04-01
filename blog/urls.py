from django.urls import path
from . import views

urlpatterns = [
    path('', views.homePage, name='home'),
    path('post_detail/<str:slug>/', views.blogDetail, name='post_detail')
]
