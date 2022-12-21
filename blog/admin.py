from django.contrib import admin
from .models import Author, Post, Tag
# Register your models here.


class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_filter = ("author", "title",)
    list_display = ("content", "author",)


class AuthorAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name",)


class TagAdmin(admin.ModelAdmin):
    list_display = ("caption",)


admin.site.register(Post, PostAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Tag, TagAdmin)
