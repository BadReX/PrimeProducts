from django.conf.urls import url
from django.contrib import admin
from . import views as userAuth_views
from django.contrib.auth import views as auth_views


urlpatterns = [
    #url(r'^$', userAuth_views.home, name='home'),
    url(r'^login/$', auth_views.login, {'template_name': 'login.html'}, name='login'),
    url(r'^logout/$', auth_views.logout, {'next_page': 'login'}, name='logout'),
    url(r'^signup/$', userAuth_views.signup, name='signup'),
]
