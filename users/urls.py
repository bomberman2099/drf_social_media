from django.urls import path
from users import views
from rest_framework_simplejwt import views as jwt_views
urlpatterns = [
    path('posts/', views.PostList.as_view(), name='post_list'),
    path('posts/<int:pk>/', views.PostDetail.as_view(), name='post_detail'),
    path('signup/', views.SignUpVIew.as_view(), name='signup'),
    path('login/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token-refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
]
