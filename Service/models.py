import random
import string
from django.db import models
from services.mixins import DateMixin
from services.uploader import Uploader
from django.template.defaultfilters import slugify


class Services(DateMixin):
    title = models.CharField(max_length=255)
    slug = models.SlugField(null=True, blank=True)
    logo = models.CharField(max_length=255)
    photo = models.ImageField(upload_to=Uploader.services_photo)
    content = models.CharField(max_length=255)

    def __str__(self):
        return self.title

    def generate_random_string(self, length=4):
        characters = string.ascii_letters + string.digits
        return ''.join(random.choice(characters) for _ in range(length))

    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.title)
            unique_slug = base_slug
            while Services.objects.filter(slug=unique_slug).exists():
                unique_slug = f"{base_slug}-{self.generate_random_string()}"
            self.slug = unique_slug
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'Service'
        verbose_name_plural = 'Services'


class ServiceProperty(DateMixin):
    # up_title = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    description = models.TextField()
    icon = models.CharField(max_length=255)
    photo = models.ImageField(upload_to=Uploader.services_property_photo)
    services = models.ForeignKey(Services, on_delete=models.CASCADE, related_name='services_property')

    def __str__(self):
        return f"{self.title}"

    class Meta:
        verbose_name = 'Service Property'
        verbose_name_plural = 'Service Property'


class ServicesPropertyDetails(DateMixin):
    title = models.CharField(max_length=255)
    content = models.CharField(max_length=255)
    services_property = models.ForeignKey(ServiceProperty, on_delete=models.CASCADE, related_name='services_property_details')

    def __str__(self):
        return f"{self.services_property.services.title}' property details {self.title}"

    class Meta:
        verbose_name = 'Services Property Details'
        verbose_name_plural = 'Services Property Details'


class LastWorks(DateMixin):
    company_name = models.CharField(max_length=255)
    photo = models.ImageField(upload_to=Uploader.services_category_last_works)
    link_url = models.URLField(max_length=200, null=True, blank=True)
    services_property = models.ForeignKey(ServiceProperty, on_delete=models.CASCADE, related_name='services_property_last_works')

    def __str__(self):
        return f"{self.services_property.services.title}'s {self.services_property.title} property {self.company_name}'s last work"

    class Meta:
        verbose_name = 'Last Work'
        verbose_name_plural = 'Last Work'


class Package(DateMixin):
    package_name = models.CharField(max_length=255)
    price_period = models.CharField(max_length=50)
    price = models.FloatField()
    color = models.CharField(max_length=255)
    symbol = models.CharField(max_length=255)
    services_property = models.ForeignKey(ServiceProperty, on_delete=models.CASCADE, related_name='services_property_packages')

    def __str__(self):
        return f"{self.services_property.services.title}'s {self.services_property.title} category {self.package_name}'s package name"


    class Meta:
        verbose_name = 'Package'
        verbose_name_plural = 'Package'


class PackageProperty(DateMixin):
    property_name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=False)
    # icon = models.ImageField(upload_to=Uploader.services_package_icon)
    package = models.ForeignKey(Package, on_delete=models.CASCADE, related_name='package_property')

    def __str__(self):
        return f"{self.package.package_name}'s {self.property_name} property"

    class Meta:
        verbose_name = 'Package Property'
        verbose_name_plural = 'Package Property'
