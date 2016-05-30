from django.shorcuts import render

def home(request):
    return render(
        request,
        "home.html",
        {"site_name": "wps_blog"},
    )
