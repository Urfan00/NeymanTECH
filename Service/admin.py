from django.contrib import admin
from .models import LastWorks, Package, PackageProperty, ServiceProperty, Services, ServicesPropertyDetails



class ServicesAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'slug', 'logo', 'photo', 'content', 'created_at', 'updated_at']
    list_display_links = ['id', 'title']
    search_fields = ['title', 'slug']


class ServicePropertyAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'photo', 'services', 'created_at', 'updated_at']
    list_display_links = ['id','title']
    search_fields = ['title', 'services__title', 'services__slug']


class ServicesPropertyDetailsAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'content', 'services_property', 'created_at', 'updated_at']
    list_display_links = ['id', 'title']
    search_fields = ['title', 'services_property__up_title', 'services_property__down_title']


class LastWorksAdmin(admin.ModelAdmin):
    list_display = ['id', 'company_name', 'photo', 'link_url', 'services_property', 'created_at', 'updated_at']
    list_display_links = ['id', 'company_name']
    search_fields = ['company_name', 'services_property__title']


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
