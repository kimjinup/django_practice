# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.

from .models import Post


class PostAdmin(admin.ModelAdmin):
	list_display = ('title', 'slug', 'author', 'publish', 'status',)
	list_filter = ('status', 'created', 'publish', 'author',)
	search_fields = ('title', 'body',)
	prepopulated_fields = {'slug': ('title',)}
	raw_id_fields = ('author',)
	date_hierachy = 'publish'
	ordering = ['status', 'publish']

admin.site.register(Post, PostAdmin)
