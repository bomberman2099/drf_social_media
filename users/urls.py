from django.urls import path
from users import views

urlpatterns = [
    path('posts/', views.PostList.as_view(), name='post_list'),

]
