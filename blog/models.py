from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.urls import reverse
from django.utils.text import slugify

# Create your models here.


class Author(models.Model):
    first_name = models.CharField(max_length=20, default="")
    last_name = models.CharField(max_length=20, default="")

    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return self.full_name()


class Tag(models.Model):
    caption = models.CharField(max_length=60, default="")


class Post(models.Model):
    title = models.CharField(max_length=30, default="")
    excerpt = models.CharField(max_length=200, default="")
    content = models.CharField(max_length=3000, default="")
    image = models.CharField(max_length=300, default="")
    date = models.DateField()
    slug = models.SlugField(default="", blank=True, null=False, db_index=True)
    author = models.ForeignKey(
        Author, on_delete=models.CASCADE, related_name="posts")
    tag = models.ManyToManyField(Tag)
