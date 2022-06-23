from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from . import models


# Register your models here.
@admin.register(models.Post)
class PostAdmin(SummernoteModelAdmin):

    prepopulated_fields = {'slug': ('title',)}
    list_filter = ('created_on', 'category')
    search_fields = ['author', 'content', 'title', 'category']
    list_display = ('title', 'slug', 'created_on')
    summernote_fields = ('content')


@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'describe')


@admin.register(models.Profile)
class UserProfile(admin.ModelAdmin):
    list_display = ('user', 'bio')
    list_filter = ('user',)
    search_fields = ['user', 'post']


@admin.register(models.Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'body', 'post', 'created_on')
    list_filter = ('created_on',)
    search_fields = ('name', 'email', 'body')
