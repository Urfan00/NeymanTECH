from django.urls import path
from .views import (BlogCategoryListCreateAPIView,
                    BlogCategoryRetrieveUpdateDestroyAPIView,
                    BlogListCreateAPIView,
                    BlogRetrieveUpdateDestroyAPIView,
                    TagListCreateAPIView,
                    TagRetrieveUpdateDestroyAPIView)


urlpatterns = [

    path('blog_category/', BlogCategoryListCreateAPIView.as_view(), name='blog_category'),
    path('blog_category/<int:pk>', BlogCategoryRetrieveUpdateDestroyAPIView.as_view(), name='blog_category'),

    path('tag/', TagListCreateAPIView.as_view(), name='tag'),
    path('tag/<int:pk>', TagRetrieveUpdateDestroyAPIView.as_view(), name='tag'),

    path('blog/', BlogListCreateAPIView.as_view(), name='blog'),
    path('blog/<slug:slug>', BlogRetrieveUpdateDestroyAPIView.as_view(), name='blog'),

]
