from django.urls import path
from .views import (CollaboratorsListCreateAPIView,
                    CollaboratorsReadUpdateDeleteView,
                    ContactCardCreateAPIView,
                    ContactListCreateAPIView,
                    ContactReadUpdateDeleteView,
                    FAQListCreateAPIView,
                    FAQReadUpdateDeleteView,
                    FeedBackListCreateAPIView,
                    FeedBackReadUpdateDeleteView,
                    OurTeamListCreateAPIView,
                    OurTeamReadUpdateDeleteView,
                    SliderListCreateAPIView,
                    SliderReadUpdateDeleteView,
                    SubscriberReadUpdateDeleteView,
                    SubscribersEmailListCreateAPIView,
                    index
                    )



urlpatterns = [

    path('collaborator/', CollaboratorsListCreateAPIView.as_view(), name='collaborator'),
    path('collaborator/<int:pk>', CollaboratorsReadUpdateDeleteView.as_view(), name='collaborator'),

    path('subscribe/', SubscribersEmailListCreateAPIView.as_view(), name='subscribe'),
    path('subscribe/<int:pk>', SubscriberReadUpdateDeleteView.as_view(), name='subscribe'),

    path('contact/', ContactListCreateAPIView.as_view(), name='contact'),
    path('contact/<int:pk>', ContactReadUpdateDeleteView.as_view(), name='contact'),

    path('slider/', SliderListCreateAPIView.as_view(), name='slider'),
    path('slider/<int:pk>', SliderReadUpdateDeleteView.as_view(), name='slider'),

    path('feedback/', FeedBackListCreateAPIView.as_view(), name='feedback'),
    path('feedback/<int:pk>', FeedBackReadUpdateDeleteView.as_view(), name='feedback'),

    path('faq/', FAQListCreateAPIView.as_view(), name='faq'),
    path('faq/<int:pk>', FAQReadUpdateDeleteView.as_view(), name='faq'),

    path('our_team/', OurTeamListCreateAPIView.as_view(), name='our_team'),
    path('our_team/<int:pk>', OurTeamReadUpdateDeleteView.as_view(), name='our_team'),

    path('contact_card/', ContactCardCreateAPIView.as_view(), name='contact_card'),

    path('', index, name='index')

]
