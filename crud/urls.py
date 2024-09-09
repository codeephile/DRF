from django.urls import path

from crud.views.booklist_views import (
    book_list,
    book_create,
    book_detail,
    book_update,
    book_delete,
)

urlpatterns = [
    path('booklist/', book_list, name='book_list'),
    path('booklist/create/', book_create, name='book_create'),
    path('booklist/<int:pk>/', book_detail, name='book_detail'),
    path('booklist/<int:pk>/update/', book_update, name='book_update'),
    path('booklist/<int:pk>/delete/', book_delete, name='book_delete'),
]

# <int:pk> for primarykey(id)=