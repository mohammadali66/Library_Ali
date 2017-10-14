from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^categorybookshome/$', views.CategoryBooksHomeAPIView.as_view(), name='categorybookshome'),        
#     url(r'^book/(?P<slug>[\w-]+)/$', views.getBookDetail, name="getBookDetail"),
#     url(r'^categoryall/$', views.getBooksByCategories),
#     url(r'^category/(?P<categorySlug>[\w-]+)/$', views.getBooksByCategory),
#     url(r'^categoryall2/$', view2.as_view()),
    #url(r'^invoices/(?P<pk>[0-9]+)/$', views.invoice_detail),
]
