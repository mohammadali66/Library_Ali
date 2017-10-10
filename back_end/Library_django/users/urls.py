from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^register/$', views.UserRegisterView.as_view(), name='register'),
    
    #url(r'^invoices/(?P<pk>[0-9]+)/$', views.invoice_detail),
]
