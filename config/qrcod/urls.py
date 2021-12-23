'''
Urls for shortener app qrcode/urls.py
'''

from django.urls import path

from . import views

appname = "shortener"

urlpatterns = [

    path("qrcod/", views.qrcode_view, name="qrcod")

]
