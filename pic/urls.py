from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns=[
    url(r'^$',views.pic,name='ftPic'),
    url(r'^picture/(\d+)',views.picture,name ='picture')

]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
