from django.contrib import admin
from .models import Author, Comment, Post, Tag
# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_filter = ("author", "tags", "date",)
    list_display = ("title", "date", "author",)
    prepopulated_fields = {"slug": ("title",)}

class CommentsAdmin(admin.ModelAdmin):
    list_display = ("text","user_name","user_email","post")

admin.site.register(Post, PostAdmin)
admin.site.register(Author)
admin.site.register(Tag)
admin.site.register(Comment,CommentsAdmin)