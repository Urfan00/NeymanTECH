from django.shortcuts import render
from rest_framework import filters
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import FAQ, Collaborators, ContactCard, Contacts, FeedBack, OurTeam, Slider, Subscribers
from .serializers import (CollaboratorsSerializers,
                          ContactCardSerializer,
                          ContactSerializers,
                          FAQSerializer,
                          FeedBackSerializers,
                          OurTeamSerializer,
                          SliderSerializers,
                          SubscribersEmailSerializer)


def index(request):
    return render(request, 'index.html')


# Collaborator GET & POST
class CollaboratorsListCreateAPIView(ListCreateAPIView):
    queryset = Collaborators.objects.all()
    filter_backends = [filters.SearchFilter]
    search_fields =  ['name']
    serializer_class = CollaboratorsSerializers


# Collaborator GET & PUT & PATCH & DELETE
class CollaboratorsReadUpdateDeleteView(RetrieveUpdateDestroyAPIView):
    queryset = Collaborators.objects.all()
    serializer_class = CollaboratorsSerializers


# Subscriber GET & POST
class SubscribersEmailListCreateAPIView(ListCreateAPIView):
    queryset = Subscribers.objects.all()
    filter_backends = [filters.SearchFilter]
    search_fields = ['email']
    serializer_class = SubscribersEmailSerializer


# Subscriber GET & PUT & DELETE
class SubscriberReadUpdateDeleteView(RetrieveUpdateDestroyAPIView):
    queryset = Subscribers.objects.all()
    serializer_class = SubscribersEmailSerializer


# Contact GET & POST
class ContactListCreateAPIView(ListCreateAPIView):
    queryset = Contacts.objects.all()
    filter_backends = [filters.SearchFilter]
    search_fields = ['fullname', 'email', 'phone_number']
    serializer_class = ContactSerializers


# Contact GET & PUT & PATCH & DELETE
class ContactReadUpdateDeleteView(RetrieveUpdateDestroyAPIView):
    queryset = Contacts.objects.all()
    serializer_class = ContactSerializers


# Slider GET & POST
class SliderListCreateAPIView(ListCreateAPIView):
    queryset = Slider.objects.all()
    filter_backends = [filters.SearchFilter]
    search_fields = ['slider_header']
    serializer_class = SliderSerializers


# Slider GET & PUT & PATCH & DELETE
class SliderReadUpdateDeleteView(RetrieveUpdateDestroyAPIView):
    queryset = Slider.objects.all()
    serializer_class = SliderSerializers


# FeedBack GET & POST
class FeedBackListCreateAPIView(ListCreateAPIView):
    queryset = FeedBack.objects.all()
    filter_backends = [filters.SearchFilter]
    search_fields = ['fullname']
    serializer_class = FeedBackSerializers


# FeedBack GET & PUT & PATCH & DELETE
class FeedBackReadUpdateDeleteView(RetrieveUpdateDestroyAPIView):
    queryset = FeedBack.objects.all()
    serializer_class = FeedBackSerializers


# FAQ GET & POST
class FAQListCreateAPIView(ListCreateAPIView):
    queryset = FAQ.objects.all()
    filter_backends = [filters.SearchFilter]
    search_fields = ['question']
    serializer_class = FAQSerializer


# FAQ GET & PUT & PATCH & DELETE
class FAQReadUpdateDeleteView(RetrieveUpdateDestroyAPIView):
    queryset = FAQ.objects.all()
    serializer_class = FAQSerializer


# Our Team GET & POST
class OurTeamListCreateAPIView(ListCreateAPIView):
    queryset = OurTeam.objects.all()
    filter_backends = [filters.SearchFilter]
    search_fields = ['fullname']
    serializer_class = OurTeamSerializer


# Our Team GET & PUT & PATCH & DELETE
class OurTeamReadUpdateDeleteView(RetrieveUpdateDestroyAPIView):
    queryset = OurTeam.objects.all()
    serializer_class = OurTeamSerializer


# Contact Card GET & POST
class ContactCardCreateAPIView(ListCreateAPIView):
    queryset = ContactCard.objects.order_by('-created_at').all()[:1]
    filter_backends = [filters.SearchFilter]
    serializer_class = ContactCardSerializer
