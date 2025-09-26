from rest_framework import serializers
from .models import Post, MyUser, ProfileUser


class PostSerializer(serializers.ModelSerializer):
    liked_posts = serializers.SerializerMethodField()
    class Meta:
        model = Post
        fields = '__all__'

    def get_liked_posts(self, obj):
        return obj.liked_posts