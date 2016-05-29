from django.conf.urls import url
from django.contrib import admin

from wpsblog.views import home, room, news

# MVC
# M_Model: DB ( Data ) & Business Logic ( * )
# V_ViewL HTML, CSS, .. -> Templatae/Client
# C_Controller: View, Model..

# 이밖에 패턴들...
# MVVM => Model View View Model
# MVW => Model View Whatever


# MVC 제작의 가장 좋은 프로세스 개발은 아래와 같이 한다.
# Model -> 더 무겁게
# Controller -> 더 가볍게 ( 즉, 기능이 Controller -> Model..)

urlpatterns = [
    url(r'^admin/', admin.site.urls),

    url(r'^$', home),
    url(r'^rooms/(?P<room_id>\d+)/$', room),

    url(r'^news/$', news),
    
]
