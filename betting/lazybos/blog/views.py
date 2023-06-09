from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from .models import Post, Comment
from .forms import PostForm, CommentForm


class PostListView(View):
    def get(self, request):
        posts = Post.objects.all()
        return render(request, 'post_list.html', {'posts': posts})


class PostDetailView(View):
    def get(self, request, pk):
        post = get_object_or_404(Post, pk=pk)
        comments = Comment.objects.filter(post=post)
        return render(request, 'post_detail.html', {'post': post, 'comments': comments})


@method_decorator(login_required, name='dispatch')
class PostCreateView(View):
    def get(self, request):
        form = PostForm()
        return render(request, 'post_form.html', {'form': form})

    def post(self, request):
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('post_detail', pk=post.pk)
        return render(request, 'post_form.html', {'form': form})


@method_decorator(login_required, name='dispatch')
class PostUpdateView(View):
    def get(self, request, pk):
        post = get_object_or_404(Post, pk=pk)
        form = PostForm(instance=post)
        return render(request, 'post_form.html', {'form': form})

    def post(self, request, pk):
        post = get_object_or_404(Post, pk=pk)
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('post_detail', pk=post.pk)
        return render(request, 'post_form.html', {'form': form})


@method_decorator(login_required, name='dispatch')
class PostDeleteView(View):
    def get(self, request, pk):
        post = get_object_or_404(Post, pk=pk)
        return render(request, 'post_confirm_delete.html', {'post': post})

    def post(self, request, pk):
        post = get_object_or_404(Post, pk=pk)
        post.delete()
        return redirect('post_list')


class CommentCreateView(View):
    def get(self, request, pk):
        post = get_object_or_404(Post, pk=pk)
        form = CommentForm()
        return render(request, 'comment_form.html', {'post': post, 'form': form})

    def post(self, request, pk):
        post = get_object_or_404(Post, pk=pk)
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('post_detail', pk=post.pk)
        return render(request, 'comment_form.html', {'post': post, 'form': form})
