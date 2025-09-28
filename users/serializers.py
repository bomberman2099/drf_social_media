from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken

from .models import Post, MyUser, ProfileUser


class PostSerializer(serializers.ModelSerializer):
    liked_posts = serializers.SerializerMethodField()
    class Meta:
        model = Post
        fields = '__all__'

    def get_liked_posts(self, obj):
        return obj.liked_posts


class MyUserSerializer(serializers.ModelSerializer):
    password = serializers.SerializerMethodField(write_only=True)
    token = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = MyUser
        fields = ('id','username', 'password', 'email', 'token')


    def create(self, validated_data):
        user = MyUser.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email', ''],
            password=validated_data['password']
        )
        return user


    def get_token(self, obj):
        refresh = RefreshToken.for_user(obj)
        return {
            'refresh': str(refresh),
            'access': str(refresh.access_token)
        }