# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404

# Create your views here.

from blog.models import Post

def post_list(request):
	posts = Post.published.all()
	return render(request, 'blog/post/list.html', {'posts': posts})

def post_detail(request, year, month, day, post):
	posts = get_object_or_404(Post, slug=post, status='published', publish__year=year, publish__month=month, publish__day=day)
	return render(request, 'blog/post/detail.html', {'post': post})


