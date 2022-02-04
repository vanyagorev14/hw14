from django.urls import path

from . import views

urlpatterns = [
    path('posts/', views.PostList.as_view(), name='post_list'),
    path('user/<int:pk>/', views.user_detail, name='user_detail'),
]