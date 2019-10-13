from . import views
from django.urls import path

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('post/new/', views.PostCreate.as_view(), name='post_create'),
    path('<slug:slug>/delete/', views.PostDelete.as_view(), name='post_delete'),
    path('<slug:slug>/update/', views.PostUpdate.as_view(), name='post_update'),
    path('accounts/profile/', views.ProfileList.as_view(), name='profile'),
]
