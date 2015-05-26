from django.conf.urls import patterns, url
from dango import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^convert/$', views.Convert.as_view(), name='convert'),
    url(r'^resize/$', views.Resize.as_view(), name='resize'),
    url(r'^rotate/$', views.Rotate.as_view(), name='rotate'),
    url(r'^meme/$', views.Meme.as_view(), name='meme'),
    url(r'^watermark-img/$', views.WatermarkImg.as_view(), name='watermark-img'), 
    url(r'^watermark-txt/$', views.WatermarkTxtView.as_view(), name='watermark-txt'), 
    url(r'^watermark-txt-down/(?P<id>\d+)$', views.WatermarkTxtDown.as_view(id=None), name='watermark-txt-down'),
    url(r'^watermark-txt-download/(?P<id>\d+)$', views.WatermarkTxtDownload.as_view(id=None), name='watermark-txt-download'), 
   )


