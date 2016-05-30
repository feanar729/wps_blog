from django.conf.urls import url
from django.contrib import admin

from wpsblog.views import *

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

    url(r'^$', home, name="home"),
    url(r'^rooms/(?P<room_id>\d+)/$', room, name="room"),
    url(r'^news/$', news, name="news"),
    
    url(r'^about/us/$', about, name="about"),
    url(r'^policy/terms/$', terms, name="terms"),
    url(r'^policy/privacy/$', privacy, name="privacy")
    url(r'^policy/disclaimer/$', disclaimer, name="disclaimer"),

]

# 1. about page (.../about, .../us , .../about-us/ )

# 정책
# 2. 이용약관 페이지 ( .../terms/ )
# 3. 개인정보 취급방침 페이지 ( .../privacy/ ) 
# 4. 법적고지와 책임의 한계 ( .../disclaimer/ )


