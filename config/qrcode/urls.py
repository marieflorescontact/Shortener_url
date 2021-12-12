'''
Urls for shortener app qrcode/urls.py
'''

from django.urls import path


from . import views

appname = "shortener"

urlpatterns = [


    path("qrcode/", views.qrcode_view, name="qrcode"),

]