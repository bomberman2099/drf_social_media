from django.contrib import admin
from .models import Post,ProfileUser,MyUser
# Register your models here.

admin.site.register(Post)
admin.site.register(ProfileUser)
admin.site.register(MyUser)