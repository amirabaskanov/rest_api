from django.contrib.auth import authenticate, login
from django.shortcuts import redirect, render
from rest_framework import generics
from blog.forms import SignupForm
from .models import Post
from .serializers import PostSerializer


def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('main_page')

    else:
        form = SignupForm
        return render(request, 'signup.html', {'form': form})


def main_url(request):
    return render(request, 'main.html', {})


class PostCreate(generics.CreateAPIView):
    serializer_class = PostSerializer


class PostList(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostDelete(generics.DestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer







