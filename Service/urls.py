from django.urls import path
from .views import (ServicesListCreateAPIView,
                    ServicesRetrieveUpdateDestroyAPIView,
                    ServicePropertyListCreateAPIView,
                    ServicePropertyRetrieveUpdateDestroyAPIView,
                    ServicesPropertyDetailsListCreateAPIView,
                    ServicesPropertyDetailsRetrieveUpdateDestroyAPIView,
                    LastWorksListCreateAPIView,
                    LastWorksRetrieveUpdateDestroyAPIView,
                    PackageListCreateAPIView,
                    PackageRetrieveUpdateDestroyAPIView,
                    PackagePropertyListCreateAPIView,
                    PackagePropertyRetrieveUpdateDestroyAPIView)


urlpatterns = [
    path('services/', ServicesListCreateAPIView.as_view(), name='services'),
    path('services/<slug:slug>', ServicesRetrieveUpdateDestroyAPIView.as_view(), name='services'),

    path('services_property/', ServicePropertyListCreateAPIView.as_view(), name='services_property'),
    path('services_property/<int:pk>', ServicePropertyRetrieveUpdateDestroyAPIView.as_view(), name='services_property'),

    path('services_property_details/', ServicesPropertyDetailsListCreateAPIView.as_view(), name='services_property_details'),
    path('services_property_details/<int:pk>', ServicesPropertyDetailsRetrieveUpdateDestroyAPIView.as_view(), name='services_property_details'),

    path('last_works/', LastWorksListCreateAPIView.as_view(), name='last_works'),
    path('last_works/<int:pk>', LastWorksRetrieveUpdateDestroyAPIView.as_view(), name='last_works'),

    path('package/', PackageListCreateAPIView.as_view(), name='package'),
    path('package/<int:pk>', PackageRetrieveUpdateDestroyAPIView.as_view(), name='package'),

    path('package_property/', PackagePropertyListCreateAPIView.as_view(), name='package_property'),
    path('package_property/<int:pk>', PackagePropertyRetrieveUpdateDestroyAPIView.as_view(), name='package_property'),

]
