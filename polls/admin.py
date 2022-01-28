from django.contrib import admin
from .models import Author, Citate


class CitateIn(admin.TabularInline):
    model = Citate


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
