from django.contrib import admin
from .models import Post, Comment

class CommentsInLine(admin.TabularInline):
    model = Comment
    extra = 0

class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'created', 'user']
    inlines = [CommentsInLine]

# Register your models here.
admin.site.register(Post, PostAdmin)
admin.site.register(Comment)
