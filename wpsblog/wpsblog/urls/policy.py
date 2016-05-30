from django.conf.urls import url

from wpsblog.views import *


urlpatterns = [
    url(r'terms/$', terms, name="terms"),
    url(r'privacy/$', privacy, name="privacy"),
    url(r'disclaimer/$', disclaimer, name="disclaimer"),
    ]

# 1. policy_urlpatterns 를 변수로
# 2. policy_urlpatterns 를 파일로 ( from .. import )
# 3. policy_urls 라는 모듈로 ( include 가 모듈 이름을 받을 수 있었다.)
# 4. urls
