from django.conf.urls import patterns, url
from dango import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^convert/$', views.ConvertView.as_view(), name='convert'),
    
    url(r'^convert-download/(?P<id>\d+)$', views.ConvertDownload.as_view(id=None), name='convert-download'),
    url(r'^resize/$', views.ResizeView.as_view(), name='resize'),
    
    url(r'^resize-download/(?P<id>\d+)$', views.ResizeDownload.as_view(id=None), name='resize-download'),
    url(r'^rotate/$', views.RotateView.as_view(), name='rotate'),
    
    url(r'^rotate-download/(?P<id>\d+)$', views.RotateDownload.as_view(id=None), name='rotate-download'),
    url(r'^meme/$', views.MemeView.as_view(), name='meme'),
    
    url(r'^meme-download/(?P<id>\d+)$', views.MemeDownload.as_view(id=None), name='meme-download'),
    url(r'^watermark-img/$', views.WatermarkImgView.as_view(), name='watermark-img'),
    
    url(r'^watermark-img-download/(?P<id>\d+)$', views.WatermarkImgDownload.as_view(id=None), name='watermark-img-download'), 
    url(r'^watermark-txt/$', views.WatermarkTxtView.as_view(), name='watermark-txt'), 
    
    url(r'^watermark-txt-download/(?P<id>\d+)$', views.WatermarkTxtDownload.as_view(id=None), name='watermark-txt-download'), 
   )


