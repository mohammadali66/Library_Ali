from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^register/$', views.RegisterAPIView.as_view(), name='register'),
    url(r'^login/$', views.LoginAPIView.as_view(), name='login'),
]