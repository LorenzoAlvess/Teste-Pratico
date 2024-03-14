from django.urls import path
from . import views

app_name = 'api'

urlpatterns = [
    # URLs para CRUD de Biblioteca
    path('libraries/', views.LibraryListAPIView.as_view(), name='library-list'),
    path('libraries/<int:pk>', views.LibraryDetailAPIView.as_view(), name='library-detail'),

    # URLs para CRUD de Livro
    path('libraries/<int:library_pk>/books', views.BookListAPIView.as_view(), name='book-list'),
    path('libraries/<int:library_pk>/books/<int:pk>', views.BookDetailAPIView.as_view(), name='book-detail'),
]
