from django.shortcuts import render

from wpsblog.models import Post


def detail(request, post_id):
    return render(
        request,
        "post/detail.html",
        {
            "post": Post.objects.all(),
        },
    )
