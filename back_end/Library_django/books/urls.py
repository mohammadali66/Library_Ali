from django.conf.urls import url

from . import views
 
urlpatterns = [
    url(r'^categorydetail/(?P<slug>[\w-]+)/$', views.CategoryDetailView.as_view(), name="categorydetail"),
    url(r'^bookdetail/(?P<slug>[\w-]+)/$', views.BookDetailView.as_view(), name="bookdetail"),
#     url(r'^categoryall/$', views.getBooksByCategories),
#     url(r'^category/(?P<categorySlug>[\w-]+)/$', views.getBooksByCategory),
#     url(r'^categoryall2/$', view2.as_view()),
#     #url(r'^invoices/(?P<pk>[0-9]+)/$', views.invoice_detail),
]
