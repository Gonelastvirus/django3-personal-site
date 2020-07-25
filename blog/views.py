from django.shortcuts import render, get_object_or_404
from django.http import HttpRequest
from .models import Blog
# Create your  blog views here.


def all_blog(request):
    blogs = Blog.objects.order_by('-date')
    return render(request, 'blog/all_blog.html', {'blogs': blogs})


def detail(request, blog_id):
    # pk is primary key, BLog hold title discription and more and pk gives blog_id
    blog = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'blog/detail.html', {'blog': blog})
