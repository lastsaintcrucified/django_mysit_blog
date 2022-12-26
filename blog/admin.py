from django.contrib import admin
from .models import Author, Post, Tag
# Register your models here.


class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_filter = ("author", "tags", "date")
    list_display = ("title", "author", "date")


class TagAdmin(admin.ModelAdmin):
    list_display = ("caption",)


admin.site.register(Post, PostAdmin)
admin.site.register(Author)
admin.site.register(Tag, TagAdmin)
