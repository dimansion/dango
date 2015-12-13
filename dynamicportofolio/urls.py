from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.portofolio_list, name='portofolio_list'),
]
