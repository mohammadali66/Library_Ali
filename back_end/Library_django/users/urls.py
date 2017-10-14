from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^register/$', views.UserRegisterView.as_view(), name='register'),
    url(r'^login/$', views.UserLoginView.as_view(), name='login'),
    url(r'^$', views.HomeView.as_view(), name='home'),
    
    #url(r'^invoices/(?P<pk>[0-9]+)/$', views.invoice_detail),
]
