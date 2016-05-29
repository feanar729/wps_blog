import json
import requests

from django.http.response import HttpResponse
from django.template import loader

def home(request):
    return render(
      requests,
      "home.html"
      {"site_name": "wpd blog"},
    )

def room(request, room_id):
    url = "http://api.zigbang.com/v1/items?detail=true&item_ids=" + room_id
    response = requests.get(url)
    return HttpResponse(
        response.content,
        content_type="application/json",
    )

def news(request):
   search = request.GET.get("search") # title 에 search 가 포함되어 있는가? 
   
   response = resquests.get("https://watcha.net/home/news.json?page=1&per=50")
   news_dict = response.json() #-> requests.json 
   news_list = news_dict.get("news")

   #news_items_list = news_dict.get("news")     
   #from IPython import embed; embed()

   if search:
       news_list = list(filter(
           lambda news: search in news.get('title'),
           news_list,
       ))

   return render(
        request,
        "news.html",
        {"news_list": news_list},
   )
