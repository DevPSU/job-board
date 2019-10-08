from django.views import generic
from django.shortcuts import render
from django.contrib.auth.models import User
from .models import Post

class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'

class PostDetail(generic.DetailView):
    model = Post
    template_name = 'post_detail.html'

class PostCreate(generic.CreateView):
    model = Post
    fields = ['title', 'slug', 'content']
    success_url='/'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class ProfileList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'profile.html'
