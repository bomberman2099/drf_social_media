from django.http import JsonResponse
from django.shortcuts import render

from users.models import Post
from users.serializers import PostSerializer


# Create your views here.
def post_list(request):
    posts = Post.objects.all()
    serializer = PostSerializer(posts, many=True)
    return JsonResponse(data=serializer.data, safe=False)

