'''
Urls for shortener app urlshortener/urls.py
'''

from django.urls import path

# Import the home view
from . import views

appname = "shortener"

urlpatterns = [
    # Home view
    path("", views.home_view, name="home"),
    path('register/', views.registerPage, name="register"),
    path("login/", views.loginPage, name="login"),
    path("logout/", views.loginPage, name="logout"),
    path('<str:shortened_part>', views.redirect_url_view, name='redirect')
]
