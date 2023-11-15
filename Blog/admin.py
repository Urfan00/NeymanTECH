import os
import shutil
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

    actions = ['delete_selected_with_images']

    def delete_selected_with_images(self, request, queryset):
        for obj in queryset:
            # Get the parent directory containing the image
            image_parent_directory = os.path.dirname(obj.photo.path)

            # Delete the associated image from the media folder
            if os.path.exists(obj.photo.path):
                os.remove(obj.photo.path)

            # Delete the object
            obj.delete()

            # Delete the immediate parent directory
            if os.path.exists(image_parent_directory):
                shutil.rmtree(image_parent_directory)

        self.message_user(request, "Selected blogs and their associated images have been deleted.")

    delete_selected_with_images.short_description = "Delete selected Blog"

    def get_actions(self, request):
        actions = super(BlogAdmin, self).get_actions(request)
        del actions['delete_selected']
        return actions



admin.site.register(Tag, TagAdmin)
admin.site.register(Blog, BlogAdmin)
admin.site.register(BlogCategory, BlogCategoryAdmin)
