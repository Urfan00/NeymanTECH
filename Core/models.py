import shutil
from django.db import models
from services.mixins import DateMixin
from services.uploader import Uploader
from django.conf import settings
from services.utils import delete_file_if_exists
import os



class Collaborators(DateMixin):
    name = models.CharField(max_length=255, null=True, blank=True)
    logo = models.ImageField(upload_to=Uploader.collaborators_logo)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        # Check if the instance already exists
        if self.pk:
            old_instance = Collaborators.objects.get(pk=self.pk)

            # Check if the image field is cleared
            if old_instance.logo and not self.logo:
                # Delete the old photo file
                delete_file_if_exists(os.path.join(settings.MEDIA_ROOT, str(old_instance.logo)))

            # Check if the image is changed
            if self.logo and self.logo != old_instance.logo:
                # Delete old image file if it exists
                delete_file_if_exists(os.path.join(settings.MEDIA_ROOT, str(old_instance.logo)))

        super().save(*args, **kwargs)

    def delete(self, using=None, keep_parents=False):
        # Get the path to the image file
        image_path = os.path.join(settings.MEDIA_ROOT, str(self.logo))

        # Delete the image file if it exists
        delete_file_if_exists(image_path)

        # Get the parent directory containing the image
        image_parent_directory = os.path.dirname(image_path)

        # Delete the immediate parent directory
        if os.path.exists(image_parent_directory):
            shutil.rmtree(image_parent_directory)

        super(Collaborators, self).delete(using, keep_parents)

    class Meta:
        verbose_name = "Collaborator"
        verbose_name_plural = "Collaborators"


class Subscribers(DateMixin):
    email = models.EmailField(max_length=254)

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = "Subscriber"
        verbose_name_plural = "Subscribers"


class Contacts(DateMixin):
    fullname = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    phone_number = models.CharField(max_length=255)
    service = models.CharField(max_length=255)
    message = models.TextField()

    def __str__(self):
        return f'{self.fullname}'

    class Meta:
        verbose_name = "Contact"
        verbose_name_plural = "Contacts"


class Slider(DateMixin):
    slider_image = models.ImageField(upload_to=Uploader.slider_image)
    slider_header = models.CharField(max_length=255)
    content = models.CharField(max_length=255)

    def __str__(self):
        return self.slider_header

    def save(self, *args, **kwargs):
        # Check if the instance already exists
        if self.pk:
            old_instance = Slider.objects.get(pk=self.pk)

            # Check if the image field is cleared
            if old_instance.slider_image and not self.slider_image:
                # Delete the old photo file
                delete_file_if_exists(os.path.join(settings.MEDIA_ROOT, str(old_instance.slider_image)))

            # Check if the image is changed
            if self.slider_image and self.slider_image != old_instance.slider_image:
                # Delete old image file if it exists
                delete_file_if_exists(os.path.join(settings.MEDIA_ROOT, str(old_instance.slider_image)))

        super().save(*args, **kwargs)

    def delete(self, using=None, keep_parents=False):
        # Get the path to the image file
        image_path = os.path.join(settings.MEDIA_ROOT, str(self.slider_image))

        # Delete the image file if it exists
        delete_file_if_exists(image_path)

        # Get the parent directory containing the image
        image_parent_directory = os.path.dirname(image_path)

        # Delete the immediate parent directory
        if os.path.exists(image_parent_directory):
            shutil.rmtree(image_parent_directory)

        super(Slider, self).delete(using, keep_parents)

    class Meta:
        verbose_name = "Slider"
        verbose_name_plural = "Sliders"


class FeedBack(DateMixin):
    avatar = models.ImageField(upload_to=Uploader.feedback_avatar)
    fullname = models.CharField(max_length=100)
    position = models.CharField(max_length=150)
    feedback = models.TextField()

    def __str__(self):
        return self.fullname

    def save(self, *args, **kwargs):
        # Check if the instance already exists
        if self.pk:
            old_instance = FeedBack.objects.get(pk=self.pk)

            # Check if the image field is cleared
            if old_instance.avatar and not self.avatar:
                # Delete the old photo file
                delete_file_if_exists(os.path.join(settings.MEDIA_ROOT, str(old_instance.avatar)))

            # Check if the image is changed
            if self.avatar and self.avatar != old_instance.avatar:
                # Delete old image file if it exists
                delete_file_if_exists(os.path.join(settings.MEDIA_ROOT, str(old_instance.avatar)))

        super().save(*args, **kwargs)

    def delete(self, using=None, keep_parents=False):
        # Get the path to the image file
        image_path = os.path.join(settings.MEDIA_ROOT, str(self.avatar))

        # Delete the image file if it exists
        delete_file_if_exists(image_path)

        # Get the parent directory containing the image
        image_parent_directory = os.path.dirname(image_path)

        # Delete the immediate parent directory
        if os.path.exists(image_parent_directory):
            shutil.rmtree(image_parent_directory)

        super(FeedBack, self).delete(using, keep_parents)

    class Meta:
        verbose_name = 'FeedBack'
        verbose_name_plural = 'FeedBack'


class FAQ(DateMixin):
    question = models.TextField()
    answer = models.TextField()

    def __str__(self):
        return self.question

    class Meta:
        verbose_name = 'FAQ'
        verbose_name_plural = 'FAQ'


class OurTeam(DateMixin):
    fullname = models.CharField(max_length=50)
    position = models.CharField(max_length=50)
    image = models.ImageField(upload_to=Uploader.our_team_image)
    github = models.URLField(max_length=200, null=True, blank=True)
    facebook = models.URLField(max_length=200, null=True, blank=True)
    linkedln = models.URLField(max_length=200, null=True, blank=True)
    instagram = models.URLField(max_length=200, null=True, blank=True)
    tweeter = models.URLField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.fullname

    def save(self, *args, **kwargs):
        # Check if the instance already exists
        if self.pk:
            old_instance = OurTeam.objects.get(pk=self.pk)

            # Check if the image field is cleared
            if old_instance.image and not self.image:
                # Delete the old photo file
                delete_file_if_exists(os.path.join(settings.MEDIA_ROOT, str(old_instance.image)))

            # Check if the image is changed
            if self.image and self.image != old_instance.image:
                # Delete old image file if it exists
                delete_file_if_exists(os.path.join(settings.MEDIA_ROOT, str(old_instance.image)))

        super().save(*args, **kwargs)

    def delete(self, using=None, keep_parents=False):
        # Get the path to the image file
        image_path = os.path.join(settings.MEDIA_ROOT, str(self.image))

        # Delete the image file if it exists
        delete_file_if_exists(image_path)

        # Get the parent directory containing the image
        image_parent_directory = os.path.dirname(image_path)

        # Delete the immediate parent directory
        if os.path.exists(image_parent_directory):
            shutil.rmtree(image_parent_directory)

        super(OurTeam, self).delete(using, keep_parents)

    class Meta:
        verbose_name = 'Our Team'
        verbose_name_plural = 'Our Team'


class ContactCard(DateMixin):
    email = models.EmailField(max_length=254)
    location = models.CharField(max_length=255)
    phone = models.CharField(max_length=20)
    icon = models.CharField(max_length=255, null=True)

    def __str__(self):
        return self.email
