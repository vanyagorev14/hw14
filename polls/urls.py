from django.urls import path

from . import views

urlpatterns = [
    path('', views.HomePage.as_view(), name='index'),
    path('create_post/', views.PostCreate.as_view(), name='post_create'),
    path('posts/', views.PostList.as_view(), name='post_list'),
    path('user/<int:pk>/', views.user_detail, name='user_detail'),
    # path('posts/<int:pk>/', views.post_detail, name='post_detail')
]