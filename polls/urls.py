from django.conf.urls import url

from polls import views

# views.index

urlpatterns = [
    url(r'^$', views.index),
    url(r'^hola/', views.hola),
]