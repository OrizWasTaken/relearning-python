from django.shortcuts import render, redirect
from django.http import Http404
from django.contrib.auth.decorators import login_required
from .models import Blog, Post
from .forms import BlogForm, PostForm

def check_blog_owner(request, blog):
    """Ensure a blog belongs to the current user."""
    if blog.owner != request.user:
        raise Http404

def index(request):
    """The homepage for blog host."""
    posts = Post.objects.all
    context = {'posts': posts}
    return render(request, 'blogs/index.html', context)

def blogs(request):
    """The page for all blogs."""
    blogs = Blog.objects.order_by('-date_added')
    context = {'blogs':blogs}
    return render(request, 'blogs/blogs.html', context)

def blog(request, blog_id):
    """The page of a particular blog."""
    blog = Blog.objects.get(id=blog_id)
    posts = blog.post_set.order_by('date_added')
    context = {'blog': blog, 'posts': posts}
    return render(request, 'blogs/blog.html', context)

def post(request, post_id):
    """A page for blog post."""
    post = Post.objects.get(id=post_id)
    blog = post.blog
    context = {'blog':blog, 'post':post}
    return render(request, 'blogs/post.html', context)

@login_required
def new_blog(request):
    """Add a new blog."""
    if request.method != 'POST':
        form = BlogForm()
    else:
        form = BlogForm(data=request.POST)
        if form.is_valid():
            new_blog = form.save(commit=False)
            new_blog.owner = request.user
            new_blog.save()
            return redirect('blogs:blogs')
    context = {'form': form}
    return render(request, 'blogs/new_blog.html', context)

@login_required
def new_post(request, blog_id):
    """Add a new post to a particular blog."""
    blog = Blog.objects.get(id=blog_id)
    check_blog_owner(request, blog)
    if request.method != 'POST':
        form = PostForm()
    else:
        form = PostForm(data=request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.blog = blog
            post.save()
            return redirect('blogs:blog', blog_id=blog_id)
    context = {'form': form, 'blog': blog}
    return render(request, 'blogs/new_post.html', context)

@login_required
def edit_blog(request, blog_id):
    """Edit a blog."""
    blog = Blog.objects.get(id=blog_id)
    check_blog_owner(request, blog)
    if request.method != 'POST':
        form = BlogForm(instance=blog)
    else:
        form = BlogForm(instance=blog, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('blogs:blog', blog_id=blog_id)
    context = {'blog': blog, 'form': form}
    return render(request, 'blogs/edit_blog.html', context)

@login_required
def edit_post(request, post_id):
    """Edit a blog post."""
    post = Post.objects.get(id=post_id)
    blog = post.blog
    check_blog_owner(request, blog)
    if request.method != 'POST':
        form = PostForm(instance=post)
    else:
        form = PostForm(instance=post, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('blogs:post', post_id=post_id)
    context = {'form': form, 'blog': blog, 'post': post}
    return render(request, 'blogs/edit_post.html', context)

