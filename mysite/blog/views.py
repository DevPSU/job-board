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

class PostUpdate(generic.UpdateView):
    model = Post
    fields = ['title', 'slug', 'content']
    success_url='/'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostDelete(generic.DeleteView):
    model = Post
    success_url='/accounts/profile/'

class ProfileList(generic.ListView):
    template_name = 'profile.html'
    def get_queryset(self):
        self.user = self.request.user
        return Post.objects.filter(author=self.user).order_by('-created_on')
    



    # queryset = Post.objects.filter(status=1).order_by('-created_on')
    # template_name = 'profile.html'
