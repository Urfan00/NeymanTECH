import random
import string
from django.db import models
from services.mixins import DateMixin
from services.uploader import Uploader
from ckeditor.fields import RichTextField
from django.template.defaultfilters import slugify



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
    slug = models.SlugField(null=True, blank=True)
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
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'Blog'
        verbose_name_plural = 'Blog'
