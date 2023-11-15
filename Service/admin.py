import os
import shutil
from django.contrib import admin
from .models import LastWorks, Package, PackageProperty, ServiceProperty, Services, ServicesPropertyDetails



class ServicesAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'slug', 'logo', 'photo', 'content', 'created_at', 'updated_at']
    list_display_links = ['id', 'title']
    search_fields = ['title', 'slug']
    actions = ['delete_selected_with_images']

    def delete_selected_with_images(self, request, queryset):
        for obj in queryset:
            # Get the parent directory containing the image
            image_parent_directory = os.path.dirname(os.path.dirname(obj.photo.path))

            # Delete the associated image from the media folder
            if os.path.exists(obj.photo.path):
                os.remove(obj.photo.path)

            # Delete the object
            obj.delete()

            # Delete the immediate parent directory
            if os.path.exists(image_parent_directory):
                shutil.rmtree(image_parent_directory)


        self.message_user(request, "Selected blogs and their associated images have been deleted.")

    delete_selected_with_images.short_description = "Delete selected Service"

    def get_actions(self, request):
        actions = super(ServicesAdmin, self).get_actions(request)
        del actions['delete_selected']
        return actions


class ServicePropertyAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'photo', 'services', 'created_at', 'updated_at']
    list_display_links = ['id','title']
    search_fields = ['title', 'services__title', 'services__slug']
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

    delete_selected_with_images.short_description = "Delete selected Service Property"

    def get_actions(self, request):
        actions = super(self).get_actions(request)
        del actions['delete_selected']
        return actions


class ServicesPropertyDetailsAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'content', 'services_property', 'created_at', 'updated_at']
    list_display_links = ['id', 'title']
    search_fields = ['title', 'services_property__up_title', 'services_property__down_title']


class LastWorksAdmin(admin.ModelAdmin):
    list_display = ['id', 'company_name', 'photo', 'link_url', 'services_property', 'created_at', 'updated_at']
    list_display_links = ['id', 'company_name']
    search_fields = ['company_name', 'services_property__title']
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

    delete_selected_with_images.short_description = "Delete selected Last Work"

    def get_actions(self, request):
        actions = super(LastWorksAdmin, self).get_actions(request)
        del actions['delete_selected']
        return actions


class PackageAdmin(admin.ModelAdmin):
    list_display = ['id', 'package_name', 'price_period', 'price', 'symbol', 'color', 'services_property', 'created_at', 'updated_at']
    list_display_links = ['id', 'package_name']
    search_fields = ['package_name', 'services_property__title']


class PackagePropertyAdmin(admin.ModelAdmin):
    list_display = ['id', 'property_name', 'is_active', 'package', 'created_at', 'updated_at']
    list_display_links = ['id', 'property_name']
    list_filter = ['is_active']
    search_fields = ['property_name', 'package__package_name']



admin.site.register(Services, ServicesAdmin)
admin.site.register(ServiceProperty, ServicePropertyAdmin)
admin.site.register(ServicesPropertyDetails, ServicesPropertyDetailsAdmin)
admin.site.register(LastWorks, LastWorksAdmin)
admin.site.register(Package, PackageAdmin)
admin.site.register(PackageProperty, PackagePropertyAdmin)
