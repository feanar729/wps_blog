import requests

from django.http.response import HttpResponse


def home(request):
    return HttpResponse("<h1>hello world</h1><p>This is blog</p>")


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
   
   #news_items_list = news_dict.get("news")     
   #from IPython import embed; embed()

   content = "<h1>News</h1>" +\
             "<p>This is news page.</p>" +\
             "".join([
             	"<h2>{title}</h2><img src={image_src}<p>{content}</p>".format(
             		title = news.get('title'),
                	image_src = news.get('image'),
			content = news.get('content'),
		)
             	for news
             	in news_dict["news"]
             
             ])

   return HttpResponse(
      #response.content
      #content_type="application/json" #watcha view
      content
   )
