from . import views
from django.urls import path
from django.views.generic.base import TemplateView
from django.shortcuts import redirect
urlpatterns = [
    path('home/', views.PostList.as_view(), name='home'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('accounts/login/', TemplateView.as_view(template_name='login.html'), name='login'),
    path('', lambda request: redirect('accounts/login', permanent=False)),
    path('signup/', views.SignUp.as_view(), name='signup'),
    path('profile/', TemplateView.as_view(template_name='profile.html'), name = 'profile')
] 