from rest_framework import generics
from rest_framework.response import Response
from .models import Library, Book
from .serializers import LibrarySerializer, BookSerializer

class LibraryListAPIView(generics.ListCreateAPIView):
    """
    Esta classe implementa a API para listar e criar bibliotecas.

    Atributos:
        queryset (QuerySet): Conjunto de consultas para recuperar todas as bibliotecas.
        serializer_class (Serializer): Classe de serializador para serializar/desserializar objetos Library.
    """
    queryset = Library.objects.all()
    serializer_class = LibrarySerializer

class LibraryDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    """
    Esta classe implementa a API para detalhar, atualizar e excluir bibliotecas.

    Atributos:
        queryset (QuerySet): Conjunto de consultas para recuperar todas as bibliotecas.
        serializer_class (Serializer): Classe de serializador para serializar/desserializar objetos Library.
    """
    queryset = Library.objects.all()
    serializer_class = LibrarySerializer

class BookListAPIView(generics.ListCreateAPIView):
    """
    Esta classe implementa a API para listar e criar livros.

    Atributos:
        queryset (QuerySet): Conjunto de consultas para recuperar todos os livros.
        serializer_class (Serializer): Classe de serializador para serializar/desserializar objetos Book.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    """
    Esta classe implementa a API para detalhar, atualizar e excluir livros.

    Atributos:
        queryset (QuerySet): Conjunto de consultas para recuperar todos os livros.
        serializer_class (Serializer): Classe de serializador para serializar/desserializar objetos Book.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
