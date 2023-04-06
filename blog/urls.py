from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.loginPage, name="login"),
    path('logout/', views.logoutUser, name="logout"),
    path('register/', views.registerPage, name="register"),
    path('', views.homePage, name='home'),
    path('write/', views.write, name='write-form'),
    path('post_detail/<str:slug>/', views.blogDetail, name='post_detail'),
    path('draft/', views.draftPage, name='draft-page'),
    path('edit_blog/<str:slug>/', views.updateBlog, name='edit-blog'),
    path('delete/<str:slug>/', views.deleteBlog, name='delete-blog')
]
