import os
import shutil
from django.contrib import admin
from .models import FAQ, Collaborators, ContactCard, Contacts, FeedBack, OurTeam, Subscribers, Slider


class ContactsAdmin(admin.ModelAdmin):
    list_display = ['id', 'fullname', 'email', 'phone_number', 'service', 'created_at', 'updated_at']
    list_display_links = ['id', 'fullname', 'email']
    search_fields = ['fullname', 'email', 'phone_number']


class CollaboratorsAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'logo', 'created_at', 'updated_at']
    list_display_links = ['id', 'name']
    search_fields = ['name']

    actions = ['delete_selected_with_images']

    def delete_selected_with_images(self, request, queryset):
        for obj in queryset:
            # Get the parent directory containing the image
            image_parent_directory = os.path.dirname(obj.logo.path)

            # Delete the associated image from the media folder
            if os.path.exists(obj.logo.path):
                os.remove(obj.logo.path)

            # Delete the object
            obj.delete()

            # Delete the immediate parent directory
            if os.path.exists(image_parent_directory):
                shutil.rmtree(image_parent_directory)

        self.message_user(request, "Selected blogs and their associated images have been deleted.")

    delete_selected_with_images.short_description = "Delete selected Collaborator"

    def get_actions(self, request):
        actions = super(CollaboratorsAdmin, self).get_actions(request)
        del actions['delete_selected']
        return actions


class SubscribersAdmin(admin.ModelAdmin):
    list_display = ['id', 'email', 'created_at', 'updated_at']
    list_display_links = ['id', 'email']
    search_fields = ['email']


class SliderAdmin(admin.ModelAdmin):
    list_display = ['id', 'slider_header', 'slider_image', 'content', 'created_at', 'updated_at']
    list_display_links = ['id', 'slider_header']
    search_fields = ['slider_header']

    actions = ['delete_selected_with_images']

    def delete_selected_with_images(self, request, queryset):
        for obj in queryset:
            # Get the parent directory containing the image
            image_parent_directory = os.path.dirname(obj.slider_image.path)

            # Delete the associated image from the media folder
            if os.path.exists(obj.slider_image.path):
                os.remove(obj.slider_image.path)

            # Delete the object
            obj.delete()

            # Delete the immediate parent directory
            if os.path.exists(image_parent_directory):
                shutil.rmtree(image_parent_directory)

        self.message_user(request, "Selected blogs and their associated images have been deleted.")

    delete_selected_with_images.short_description = "Delete selected Sliders"

    def get_actions(self, request):
        actions = super(SliderAdmin, self).get_actions(request)
        del actions['delete_selected']
        return actions


class FeedBackAdmin(admin.ModelAdmin):
    list_display = ['id', 'avatar', 'fullname', 'position', 'created_at', 'updated_at']
    list_display_links = ['id', 'fullname']
    search_fields = ['fullname']
    actions = ['delete_selected_with_images']

    def delete_selected_with_images(self, request, queryset):
        for obj in queryset:
            # Get the parent directory containing the image
            image_parent_directory = os.path.dirname(obj.avatar.path)

            # Delete the associated image from the media folder
            if os.path.exists(obj.avatar.path):
                os.remove(obj.avatar.path)

            # Delete the object
            obj.delete()

            # Delete the immediate parent directory
            if os.path.exists(image_parent_directory):
                shutil.rmtree(image_parent_directory)

        self.message_user(request, "Selected blogs and their associated images have been deleted.")

    delete_selected_with_images.short_description = "Delete selected FeedBack"

    def get_actions(self, request):
        actions = super(FeedBackAdmin, self).get_actions(request)
        del actions['delete_selected']
        return actions


class FAQAdmin(admin.ModelAdmin):
    list_display = ['id', 'question', 'created_at', 'updated_at']
    list_display_links = ['id', 'question']
    search_fields = ['question']


class OurTeamAdmin(admin.ModelAdmin):
    list_display = ['id', 'fullname', 'position', 'image', 'github', 'facebook', 'linkedln', 'instagram', 'tweeter', 'created_at', 'updated_at']
    list_display_links = ['id', 'fullname']
    search_fields = ['fullname']
    actions = ['delete_selected_with_images']

    def delete_selected_with_images(self, request, queryset):
        for obj in queryset:
            # Get the parent directory containing the image
            image_parent_directory = os.path.dirname(obj.image.path)

            # Delete the associated image from the media folder
            if os.path.exists(obj.image.path):
                os.remove(obj.image.path)

            # Delete the object
            obj.delete()

            # Delete the immediate parent directory
            if os.path.exists(image_parent_directory):
                shutil.rmtree(image_parent_directory)

        self.message_user(request, "Selected blogs and their associated images have been deleted.")

    delete_selected_with_images.short_description = "Delete selected Our Team"

    def get_actions(self, request):
        actions = super(OurTeamAdmin, self).get_actions(request)
        del actions['delete_selected']
        return actions


class ContactCardAdmin(admin.ModelAdmin):
    list_display = ['id', 'email', 'location', 'phone','icon', 'created_at', 'updated_at']
    list_display_links = ['id', 'email']
    search_fields = ['email']


admin.site.register(Collaborators, CollaboratorsAdmin)
admin.site.register(Subscribers, SubscribersAdmin)
admin.site.register(Contacts, ContactsAdmin)
admin.site.register(Slider, SliderAdmin)
admin.site.register(FeedBack, FeedBackAdmin)
admin.site.register(FAQ, FAQAdmin)
admin.site.register(OurTeam, OurTeamAdmin)
admin.site.register(ContactCard, ContactCardAdmin)
