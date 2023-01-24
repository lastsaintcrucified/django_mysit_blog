from django.contrib import admin
from .models import Author, Post, Tag, Comment
# Register your models here.


class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_filter = ("author", "tags", "date")
    list_display = ("title", "author", "date")


class CommentAdmin(admin.ModelAdmin):
    list_filter = ("user_name", "user_email")
    list_display = ("user_name", "user_email")


class TagAdmin(admin.ModelAdmin):
    list_display = ("caption",)


admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Author)
admin.site.register(Tag, TagAdmin)
