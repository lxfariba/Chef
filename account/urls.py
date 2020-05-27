from django.conf.urls import url
from . import views, profile


urlpatterns = [
    url(r'^register/$', views.register, name='register'),
    url(r'^login/$', views.login_view, name='login'),
    url(r'^reset_password', views.reset_password_view, name='reset_password'),
    url(r'^profile/$', profile.profile_view, name='profile'),
    url(r'^change_password/$', profile.change_password_view, name='change_password'),
    url(r'^logout/$', views.logout_view, name='logout')
 ]