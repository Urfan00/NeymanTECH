from rest_framework import serializers
from .models import (LastWorks,
                     Package,
                     PackageProperty,
                     ServiceProperty,
                     Services,
                     ServicesPropertyDetails)


class PackagePropertySeriazlier(serializers.ModelSerializer):
    class Meta:
        model = PackageProperty
        fields = ['id', 'property_name', 'is_active', 'package', 'created_at', 'updated_at']


class PackageREADSerializer(serializers.ModelSerializer):
    package_properties = PackagePropertySeriazlier(many=True, read_only=True, source='package_property')

    class Meta:
        model = Package
        fields = ['id', 'package_name', 'price_period', 'price', 'color', 'symbol', 'services_property', 'package_properties', 'created_at', 'updated_at']


class PackageCREATESerializer(serializers.ModelSerializer):
    class Meta:
        model = Package
        fields = ['id', 'package_name', 'price_period', 'price', 'color', 'symbol', 'services_property', 'created_at', 'updated_at']


class ServiceCREATESerializer(serializers.ModelSerializer):
    class Meta:
        model = Services
        fields = ['id', 'title', 'slug', 'logo', 'photo', 'content', 'created_at', 'updated_at']


class ServicePropertyCREATESerializer(serializers.ModelSerializer):
    # services=ServiceCREATESerializer()

    class Meta:
        model = ServiceProperty
        fields = ['id', 'title','description', 'photo', 'services', 'icon', 'created_at', 'updated_at']


class LastWorksSerializer(serializers.ModelSerializer):
    # services_property = ServicePropertyCREATESerializer()

    class Meta:
        model = LastWorks
        fields = ['id', 'company_name', 'photo', 'link_url', 'services_property', 'created_at', 'updated_at']


class ServicesPropertyDetailsSeriazlier(serializers.ModelSerializer):
    class Meta:
        model = ServicesPropertyDetails
        fields = ['id', 'title', 'content', 'services_property',  'created_at', 'updated_at']


class ServicePropertyREADSerializer(serializers.ModelSerializer):
    service_property_detail = ServicesPropertyDetailsSeriazlier(many=True, read_only=True, source='services_property_details')
    package = PackageREADSerializer(many=True, read_only=True, source='services_property_packages')

    class Meta:
        model = ServiceProperty
        fields = ['id', 'title','description', 'photo', 'services', 'icon', 'service_property_detail', 'package', 'created_at', 'updated_at']


class ServiceREADSerializer(serializers.ModelSerializer):
    service_details = ServicePropertyREADSerializer(many=True, read_only=True, source='services_property')

    class Meta:
        model = Services
        fields = ['id', 'title', 'slug', 'logo', 'photo', 'content', 'service_details', 'created_at', 'updated_at']
