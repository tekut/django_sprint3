from django.http import Http404
from django.shortcuts import render

posts = [
    {
        'id': 0
    },
]


def index(request):
    context = {'posts': posts}
    return render(request, 'blog/index.html', context)


def post_detail(request, id):
    try:
        post = next(post for post in posts if post['id'] == id)
    except StopIteration:
        raise Http404("No such post")
    context = {'post': post}
    return render(request, 'blog/detail.html', context)


def category_posts(request, category_slug):
    context = {'category_slug': category_slug}
    return render(request, 'blog/category.html', context)
