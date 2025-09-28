from django.http import JsonResponse
from django.shortcuts import render
from rest_framework import status, generics
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken

from users.models import Post
from users.serializers import PostSerializer, MyUserSerializer




# auth
class SignUpVIew(generics.CreateAPIView):
    serializer_class = MyUserSerializer
    permission_classes = [AllowAny]


class LogoutView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        refresh = request.data.get('refresh')
        if not refresh:
            return Response({'detail':'refresh token required.'},status=status.HTTP_401_UNAUTHORIZED)
        try:
            token = RefreshToken.for_user(request.user)
            token.blacklist()
            return Response({'detail':'logged out successfully.'},status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'detail':'logged out failed.'},status=status.HTTP_400_BAD_REQUEST)




# posts
class PostList(APIView):
    serializer_class = PostSerializer

    def get(self, request, format=None):
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = PostSerializer(data=request.data)

        if serializer.is_valid():
            serializer.validated_data['user'] = request.user
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PostDetail(APIView):
    serializer_class = PostSerializer
    def get(self, request, pk, format=None):
        post = Post.objects.get(pk=pk)
        serializer = PostSerializer(post)

        return Response(serializer.data)

    def delete(self, request, pk, format=None):
        post = Post.objects.get(pk=pk)
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def put(self, request, pk, format=None):
        post = Post.objects.get(pk=pk)
        serializer = PostSerializer(post, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

