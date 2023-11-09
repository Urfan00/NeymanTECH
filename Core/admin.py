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


class SubscribersAdmin(admin.ModelAdmin):
    list_display = ['id', 'email', 'created_at', 'updated_at']
    list_display_links = ['id', 'email']
    search_fields = ['email']


class SliderAdmin(admin.ModelAdmin):
    list_display = ['id', 'slider_header', 'slider_image', 'content', 'created_at', 'updated_at']
    list_display_links = ['id', 'slider_header']
    search_fields = ['slider_header']


class FeedBackAdmin(admin.ModelAdmin):
    list_display = ['id', 'avatar', 'fullname', 'position', 'created_at', 'updated_at']
    list_display_links = ['id', 'fullname']
    search_fields = ['fullname']


class FAQAdmin(admin.ModelAdmin):
    list_display = ['id', 'question', 'created_at', 'updated_at']
    list_display_links = ['id', 'question']
    search_fields = ['question']


class OurTeamAdmin(admin.ModelAdmin):
    list_display = ['id', 'fullname', 'position', 'image', 'github', 'facebook', 'linkedln', 'instagram', 'tweeter', 'created_at', 'updated_at']
    list_display_links = ['id', 'fullname']
    search_fields = ['fullname']


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
