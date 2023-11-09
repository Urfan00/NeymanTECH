from django.contrib import admin
from .models import Blog, BlogCategory, Tag


class TagAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    list_display_links = ['id', 'name']
    search_fields = ['name']


class BlogCategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    list_display_links = ['id', 'name']
    search_fields = ['name']


class BlogAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'photo', 'slug','date','is_active','short_descriptions', 'blog_category' ]
    list_display_links = ['id', 'title']
    list_filter = ['is_active']
    search_fields = ['title']


admin.site.register(Tag, TagAdmin)
admin.site.register(Blog, BlogAdmin)
admin.site.register(BlogCategory, BlogCategoryAdmin)
