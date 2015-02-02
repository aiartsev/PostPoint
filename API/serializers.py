__author__ = 'Alex'

from rest_framework import serializers
from API.models import Post


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('id', 'text', 'enabled')
