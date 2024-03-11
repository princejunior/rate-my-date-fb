from django.contrib import admin
from .models import Person, Post, Comment, User
# Register your models here.
admin.site.register(User)
admin.site.register(Person)
admin.site.register(Post)
admin.site.register(Comment)
