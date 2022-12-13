from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.template.loader import render_to_string
from datetime import date


# Create your views here.
all_posts = [
    {
        "slug": "hike-in-the-mountains",
        "image": "mountains.jpg",
        "author": "Towhid",
        "date": date(2022, 7, 22),
        "title": "Mountain hiking",
        "excerpt": "There's is nothing like the view you get when you are hiking on the mountin",
        "content": """
             Lorem Ipsum Dolor Amet.Lorem Ipsum Dolor AmetLorem Ipsum Dolor AmetLorem
            Ipsum Dolor AmetLorem Ipsum Dolor Amet Lorem Ipsum Dolor Amet.Lorem Ipsum
            Dolor AmetLorem Ipsum Dolor AmetLorem Ipsum Dolor AmetLorem Ipsum Dolor Amet

            Lorem Ipsum Dolor Amet.Lorem Ipsum Dolor AmetLorem Ipsum Dolor AmetLorem
            Ipsum Dolor AmetLorem Ipsum Dolor Amet Lorem Ipsum Dolor Amet.Lorem Ipsum
            Dolor AmetLorem Ipsum Dolor AmetLorem Ipsum Dolor AmetLorem Ipsum Dolor Amet

            Lorem Ipsum Dolor Amet.Lorem Ipsum Dolor AmetLorem Ipsum Dolor AmetLorem
            Ipsum Dolor AmetLorem Ipsum Dolor Amet Lorem Ipsum Dolor Amet.Lorem Ipsum
            Dolor AmetLorem Ipsum Dolor AmetLorem Ipsum Dolor AmetLorem Ipsum Dolor Amet
        """
    },
    {
        "slug": "hike-in-the-mountains",
        "image": "mountains.jpg",
        "author": "Towhid",
        "date": date(2022, 7, 22),
        "title": "Mountain hiking",
        "excerpt": "There's is nothing like the view you get when you are hiking on the mountin",
        "content": """
             Lorem Ipsum Dolor Amet.Lorem Ipsum Dolor AmetLorem Ipsum Dolor AmetLorem
            Ipsum Dolor AmetLorem Ipsum Dolor Amet Lorem Ipsum Dolor Amet.Lorem Ipsum
            Dolor AmetLorem Ipsum Dolor AmetLorem Ipsum Dolor AmetLorem Ipsum Dolor Amet

            Lorem Ipsum Dolor Amet.Lorem Ipsum Dolor AmetLorem Ipsum Dolor AmetLorem
            Ipsum Dolor AmetLorem Ipsum Dolor Amet Lorem Ipsum Dolor Amet.Lorem Ipsum
            Dolor AmetLorem Ipsum Dolor AmetLorem Ipsum Dolor AmetLorem Ipsum Dolor Amet
            
            Lorem Ipsum Dolor Amet.Lorem Ipsum Dolor AmetLorem Ipsum Dolor AmetLorem
            Ipsum Dolor AmetLorem Ipsum Dolor Amet Lorem Ipsum Dolor Amet.Lorem Ipsum
            Dolor AmetLorem Ipsum Dolor AmetLorem Ipsum Dolor AmetLorem Ipsum Dolor Amet
        """
    },
    {
        "slug": "hike-in-the-mountains",
        "image": "mountains.jpg",
        "author": "Towhid",
        "date": date(2022, 7, 22),
        "title": "Mountain hiking",
        "excerpt": "There's is nothing like the view you get when you are hiking on the mountin",
        "content": """
             Lorem Ipsum Dolor Amet.Lorem Ipsum Dolor AmetLorem Ipsum Dolor AmetLorem
            Ipsum Dolor AmetLorem Ipsum Dolor Amet Lorem Ipsum Dolor Amet.Lorem Ipsum
            Dolor AmetLorem Ipsum Dolor AmetLorem Ipsum Dolor AmetLorem Ipsum Dolor Amet

            Lorem Ipsum Dolor Amet.Lorem Ipsum Dolor AmetLorem Ipsum Dolor AmetLorem
            Ipsum Dolor AmetLorem Ipsum Dolor Amet Lorem Ipsum Dolor Amet.Lorem Ipsum
            Dolor AmetLorem Ipsum Dolor AmetLorem Ipsum Dolor AmetLorem Ipsum Dolor Amet
            
            Lorem Ipsum Dolor Amet.Lorem Ipsum Dolor AmetLorem Ipsum Dolor AmetLorem
            Ipsum Dolor AmetLorem Ipsum Dolor Amet Lorem Ipsum Dolor Amet.Lorem Ipsum
            Dolor AmetLorem Ipsum Dolor AmetLorem Ipsum Dolor AmetLorem Ipsum Dolor Amet
        """
    },
    {
        "slug": "hike-in-the-mountains",
        "image": "mountains.jpg",
        "author": "Towhid",
        "date": date(2022, 7, 22),
        "title": "Mountain hiking",
        "excerpt": "There's is nothing like the view you get when you are hiking on the mountin",
        "content": """
             Lorem Ipsum Dolor Amet.Lorem Ipsum Dolor AmetLorem Ipsum Dolor AmetLorem
            Ipsum Dolor AmetLorem Ipsum Dolor Amet Lorem Ipsum Dolor Amet.Lorem Ipsum
            Dolor AmetLorem Ipsum Dolor AmetLorem Ipsum Dolor AmetLorem Ipsum Dolor Amet

            Lorem Ipsum Dolor Amet.Lorem Ipsum Dolor AmetLorem Ipsum Dolor AmetLorem
            Ipsum Dolor AmetLorem Ipsum Dolor Amet Lorem Ipsum Dolor Amet.Lorem Ipsum
            Dolor AmetLorem Ipsum Dolor AmetLorem Ipsum Dolor AmetLorem Ipsum Dolor Amet
            
            Lorem Ipsum Dolor Amet.Lorem Ipsum Dolor AmetLorem Ipsum Dolor AmetLorem
            Ipsum Dolor AmetLorem Ipsum Dolor Amet Lorem Ipsum Dolor Amet.Lorem Ipsum
            Dolor AmetLorem Ipsum Dolor AmetLorem Ipsum Dolor AmetLorem Ipsum Dolor Amet
        """
    },
    {
        "slug": "hike-in-the-mountains",
        "image": "mountains.jpg",
        "author": "Towhid",
        "date": date(2022, 7, 22),
        "title": "Mountain hiking",
        "excerpt": "There's is nothing like the view you get when you are hiking on the mountin",
        "content": """
             Lorem Ipsum Dolor Amet.Lorem Ipsum Dolor AmetLorem Ipsum Dolor AmetLorem
            Ipsum Dolor AmetLorem Ipsum Dolor Amet Lorem Ipsum Dolor Amet.Lorem Ipsum
            Dolor AmetLorem Ipsum Dolor AmetLorem Ipsum Dolor AmetLorem Ipsum Dolor Amet

            Lorem Ipsum Dolor Amet.Lorem Ipsum Dolor AmetLorem Ipsum Dolor AmetLorem
            Ipsum Dolor AmetLorem Ipsum Dolor Amet Lorem Ipsum Dolor Amet.Lorem Ipsum
            Dolor AmetLorem Ipsum Dolor AmetLorem Ipsum Dolor AmetLorem Ipsum Dolor Amet
            
            Lorem Ipsum Dolor Amet.Lorem Ipsum Dolor AmetLorem Ipsum Dolor AmetLorem
            Ipsum Dolor AmetLorem Ipsum Dolor Amet Lorem Ipsum Dolor Amet.Lorem Ipsum
            Dolor AmetLorem Ipsum Dolor AmetLorem Ipsum Dolor AmetLorem Ipsum Dolor Amet
        """
    },
    {
        "slug": "hike-in-the-mountains",
        "image": "mountains.jpg",
        "author": "Towhid",
        "date": date(2022, 7, 22),
        "title": "Mountain hiking",
        "excerpt": "There's is nothing like the view you get when you are hiking on the mountin",
        "content": """
             Lorem Ipsum Dolor Amet.Lorem Ipsum Dolor AmetLorem Ipsum Dolor AmetLorem
            Ipsum Dolor AmetLorem Ipsum Dolor Amet Lorem Ipsum Dolor Amet.Lorem Ipsum
            Dolor AmetLorem Ipsum Dolor AmetLorem Ipsum Dolor AmetLorem Ipsum Dolor Amet

            Lorem Ipsum Dolor Amet.Lorem Ipsum Dolor AmetLorem Ipsum Dolor AmetLorem
            Ipsum Dolor AmetLorem Ipsum Dolor Amet Lorem Ipsum Dolor Amet.Lorem Ipsum
            Dolor AmetLorem Ipsum Dolor AmetLorem Ipsum Dolor AmetLorem Ipsum Dolor Amet
            
            Lorem Ipsum Dolor Amet.Lorem Ipsum Dolor AmetLorem Ipsum Dolor AmetLorem
            Ipsum Dolor AmetLorem Ipsum Dolor Amet Lorem Ipsum Dolor Amet.Lorem Ipsum
            Dolor AmetLorem Ipsum Dolor AmetLorem Ipsum Dolor AmetLorem Ipsum Dolor Amet
        """
    }

]


def get_date(post):
    return post["date"]


def starting_page(request):
    sorted_posts = sorted(all_posts, key=get_date)
    latest_posts = sorted_posts[-3:]
    return render(request, "blog/index.html", {
        "posts": latest_posts
    })


def posts(request):
    return render(request, "blog/all-posts.html", {
        "all_posts": all_posts
    })


def post_detail(request, slug):
    identified_post = next(post for post in all_posts if post['slug'] == slug)
    return render(request, "blog/post-detail.html", {
        "post": identified_post
    })
