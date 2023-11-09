from rest_framework import serializers
from .models import Blog, BlogCategory, Tag



class BlogCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogCategory
        fields = ['id', 'name', 'created_at', 'updated_at']


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id', 'name', 'created_at', 'updated_at']


class BlogCREATESerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = ['id', 'title', 'photo', 'slug','date','is_active', 'short_descriptions', 'long_descriptions', 'blog_category', 'tag', 'created_at', 'updated_at']


class BlogREADSerializer(serializers.ModelSerializer):
    blog_category = BlogCategorySerializer()
    tag = TagSerializer(many=True)

    class Meta:
        model = Blog
        fields = ['id', 'title', 'photo', 'slug','date','is_active', 'short_descriptions', 'long_descriptions', 'blog_category', 'tag', 'created_at', 'updated_at']
