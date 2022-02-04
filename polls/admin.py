from django.contrib import admin
from .models import Author, Citate
from .models import Comment, Post


class CitateIn(admin.TabularInline):
    model = Citate


class CommentIn(admin.TabularInline):
    model = Comment

@admin.register(Author)
class Admin(admin.ModelAdmin):
    list_display = ['name', 'birthday', 'birthday_loc', 'description']
    list_filter = ['name', 'birthday_loc']
    search_fields = ['name']
    inlines = CitateIn


@admin.register(Citate)
class AdminC(admin.ModelAdmin):
    list_display = ['text', 'author']
    list_filter = ['author']


@admin.register(Post)
class PostAdm(admin.ModelAdmin):
    list_display = ['author', 'title', 'brief_description', 'publish_date', 'full_description', 'posted']
    list_filter = ['author']
    search_fields = ['title']
    inlines = [CommentIn]


@admin.register(Comment)
class CommAdm(admin.ModelAdmin):
    list_display = ['username', 'text', 'post', 'posted_comment']
    list_filter = ['username']
    search_fields = ['username']
    ordering = ['post', 'posted_comment']
