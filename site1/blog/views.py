# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404

# Create your views here.

from blog.models import Post

def post_list(request):
	posts = Post.published.all()
	return render(request


