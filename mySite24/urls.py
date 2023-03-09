from django.conf.urls import url
from django.contrib import admin
from mySite24.views import studentsView, pupilsView, uch_revView, uch_ostView, uchView_find, uchView_add, auto, indexView, registView, hudView, naukView, mangaView, partView, speedtestView, calkView, randomView
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^students/', studentsView),
    url(r'^pupils/', pupilsView),
    url(r'^uch_rev/', uch_revView),
    url(r'^uch_ost/', uch_ostView),
    url(r'^uch_find/', uchView_find),
    url(r'^uch_add/', uchView_add),
    url(r'^auto/', auto),
    url(r'^index/', indexView),
    url(r'^regist/', registView),
    url(r'^hud/', hudView),
    url(r'^nauk/', naukView),
    url(r'^manga/', mangaView),
    url(r'^part/', partView),
    url(r'^speedtest/', speedtestView),
    url(r'^calk/', calkView),
    url(r'^random/',randomView),
]

