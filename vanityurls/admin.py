from django.contrib import admin

from .models import Category, VanityUrl


@admin.register(Category)
class VanityUrlAdmin(admin.ModelAdmin):

    list_display = ['name']


@admin.register(VanityUrl)
class VanityUrlAdmin(admin.ModelAdmin):

    list_display = ['vanity_url', 'target', 'code', 'category']
