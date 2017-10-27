from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^categorybookshome/$', views.CategoryBooksHomeAPIView.as_view(), name='categorybookshome'),
    url(r'^categorymenu/$', views.CategoryMenuAPIView.as_view(), name='categorymenu'),
    url(r'^category/(?P<slug>[\w-]+)/$', views.CategoryDetailAPIView.as_view(), name='categorydetail'),
    url(r'^categorybrief/(?P<slug>[\w-]+)/$', views.CategoryDetailBriefAPIView.as_view(), name='categorydetailbrief'),
    url(r'^bookscategory/(?P<categoryslug>[\w-]+)/$', views.BooksOfOneCategoryAPIView.as_view(), name='bookscategory'),
    url(r'^bookdetail/(?P<slug>[\w-]+)/$', views.BookDetailAPIView.as_view(), name='bookdetail'),
    url(r'^addbook/(?P<slug>[\w-]+)/$', views.AddBookToBooksListUserAPIView.as_view(), name='addbook'),
    url(r'^booksuser/$', views.BooksOfLoggedUserAPIView.as_view(), name='booksuser'),
    
    
    url(r'^note/(?P<bookslug>[\w-]+)/$', views.NoteAPIView.as_view(), name='note'),
    url(r'^noteupdatedelete/(?P<pk>\d+)/$', views.NoteUpdateDeleteAPIView.as_view(), name='noteupdatedelete'),
      
#     url(r'^book/(?P<slug>[\w-]+)/$', views.getBookDetail, name="getBookDetail"),
#     url(r'^categoryall/$', views.getBooksByCategories),
#     url(r'^category/(?P<categorySlug>[\w-]+)/$', views.getBooksByCategory),
#     url(r'^categoryall2/$', view2.as_view()),
    #url(r'^invoices/(?P<pk>[0-9]+)/$', views.invoice_detail),
]
