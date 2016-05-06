from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^top/', views.top_twenty, name='top_twenty'),
    url(r'^users/', views.users, name='users'),
    url(r'^(?P<movie_id>[0-9]+)/$', views.movie, name='movie'),
    url(r'^rater/(?P<user_id>[0-9]+)/$', views.raterer, name='rater'),
]
