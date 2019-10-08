from . import views
from django.urls import path

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('post/new/', views.PostCreate.as_view(), name='post_create'),
    path('accounts/profile/', views.ProfileList.as_view(), name='profile'),
]
