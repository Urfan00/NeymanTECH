import random
import shutil
import string
from django.db import models
from services.mixins import DateMixin
from services.uploader import Uploader
from ckeditor.fields import RichTextField
from django.template.defaultfilters import slugify
from django.conf import settings
from services.utils import delete_file_if_exists
import os



class BlogCategory(DateMixin):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Blog Category'
        verbose_name_plural = 'Blog Category'


class Tag(DateMixin):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Tag'
        verbose_name_plural = 'Tags'


class Blog(DateMixin):
    title = models.CharField(max_length=255)
    photo = models.ImageField(upload_to=Uploader.blog_image)
    slug = models.SlugField(null=True, blank=True, unique=True)
    short_descriptions = RichTextField()
    long_descriptions = RichTextField()
    blog_category = models.ForeignKey(BlogCategory, on_delete=models.CASCADE, related_name='blog_category')
    tag = models.ManyToManyField(Tag, related_name='blog_tag')
    date = models.DateField(null=True)
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    def generate_random_string(self, length=4):
        characters = string.ascii_letters + string.digits
        return ''.join(random.choice(characters) for _ in range(length))

    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.title)
            unique_slug = base_slug
            while Blog.objects.filter(slug=unique_slug).exists():
                unique_slug = f"{base_slug}-{self.generate_random_string()}"
            self.slug = unique_slug

        # Check if the instance already exists
        if self.pk:
            old_instance = Blog.objects.get(pk=self.pk)

            # Check if the image field is cleared
            if old_instance.photo and not self.photo:
                # Delete the old photo file
                delete_file_if_exists(os.path.join(settings.MEDIA_ROOT, str(old_instance.photo)))

            # Check if the image is changed
            if self.photo and self.photo != old_instance.photo:
                # Delete old image file if it exists
                delete_file_if_exists(os.path.join(settings.MEDIA_ROOT, str(old_instance.photo)))

        super().save(*args, **kwargs)

    def delete(self, using=None, keep_parents=False):
        # Get the path to the image file
        image_path = os.path.join(settings.MEDIA_ROOT, str(self.photo))

        # Delete the image file if it exists
        delete_file_if_exists(image_path)

        # Get the parent directory containing the image
        image_parent_directory = os.path.dirname(image_path)

        # Delete the immediate parent directory
        if os.path.exists(image_parent_directory):
            shutil.rmtree(image_parent_directory)

        super(Blog, self).delete(using, keep_parents)

    class Meta:
        verbose_name = 'Blog'
        verbose_name_plural = 'Blog'
