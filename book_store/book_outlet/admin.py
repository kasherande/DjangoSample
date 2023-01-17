from django.contrib import admin
from .models import Address, Book, Author
# Register your models here.


class BookAdmin(admin.ModelAdmin):
    # readonly_fields = ("slug",)
    prepopulated_fields = {"slug": ("title", )}
    list_filter = ("author", "rating")
    list_display = ("title", "author")

# class AuthorAdmin(admin.ModelAdmin):
    # list_filter = ("author","address")
    # list_display = ("author","address")

admin.site.register(Book, BookAdmin)
admin.site.register(Author)
# admin.site.register(Author, AuthorAdmin)
admin.site.register(Address)