from django.db import models
from services.mixins import DateMixin
from services.uploader import Uploader



class Collaborators(DateMixin):
    name = models.CharField(max_length=255, null=True, blank=True)
    logo = models.ImageField(upload_to=Uploader.collaborators_logo)

    def __str__(self):
        return self.name

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


