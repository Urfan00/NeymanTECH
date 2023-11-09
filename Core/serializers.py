from rest_framework import serializers
from .models import FAQ, Collaborators, ContactCard, Contacts, FeedBack, OurTeam, Slider, Subscribers



# Collaborator Serializer
class CollaboratorsSerializers(serializers.ModelSerializer):
    class Meta:
        model = Collaborators
        fields = ['id', 'name', 'logo', 'created_at', 'updated_at']


# Subscriber Serializer
class SubscribersEmailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscribers
        fields = ['id', 'email', 'created_at', 'updated_at']


# Contact Serializer
class ContactSerializers(serializers.ModelSerializer):
    class Meta:
        model = Contacts
        fields = ['id', 'fullname', 'email', 'phone_number', 'service', 'message', 'created_at', 'updated_at']


# Slider Serializer
class SliderSerializers(serializers.ModelSerializer):
    class Meta:
        model = Slider
        fields = ['id', 'slider_image', 'slider_header', 'content', 'created_at', 'updated_at']


# FeedBack serializer
class FeedBackSerializers(serializers.ModelSerializer):
    class Meta:
        model = FeedBack
        fields = ['id', 'avatar', 'fullname', 'position', 'feedback', 'created_at', 'updated_at']


# FAQ Serializer
class FAQSerializer(serializers.ModelSerializer):
    class Meta:
        model = FAQ
        fields = ['id', 'question', 'answer', 'created_at', 'updated_at']


# Our Team Serializer
class OurTeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = OurTeam
        fields = ['id', 'fullname', 'position', 'image', 'github', 'facebook', 'linkedln', 'instagram', 'tweeter', 'created_at', 'updated_at']

# Contact Card
class ContactCardSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactCard
        fields = ['id', 'email', 'location', 'phone','icon', 'created_at', 'updated_at']
