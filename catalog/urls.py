from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('create_book/', views.BookCreate.as_view(), name='create_book'),
    path('book_list/', views.BookList.as_view(), name='book_list'),
    path('book_detail/<int:pk>', views.BookDetail.as_view(), name='book_detail'),
    path('my_view', views.my_view, name='my_view'),
    path('signup/', views.SignUpView.as_view(), name='signup'),
    path('profile/', views.CheckedOutBooksByUserVIew.as_view(), name='profile')
]
