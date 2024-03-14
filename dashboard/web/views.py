from django.shortcuts import render
from api.models import Library, Book
from django.db.models import Count
from datetime import datetime, timedelta

def home(request):
    """
    Renderiza a página inicial.

    Args:
        request (HttpRequest): O objeto HttpRequest que representa a requisição HTTP.

    Returns:
        HttpResponse: A resposta HTTP renderizada.
    """
    return render(request, 'pages/home.html')

def bibliotecas(request):
    """
    Renderiza a página de bibliotecas.

    Args:
        request (HttpRequest): O objeto HttpRequest que representa a requisição HTTP.

    Returns:
        HttpResponse: A resposta HTTP renderizada contendo a lista de bibliotecas.
    """
    bibliotecas = Library.objects.all()
    return render(request, 'pages/bibliotecas.html', {'bibliotecas': bibliotecas})

def livros(request, biblioteca_id):
    """
    Renderiza a página de livros de uma biblioteca específica.

    Args:
        request (HttpRequest): O objeto HttpRequest que representa a requisição HTTP.
        biblioteca_id (int): O ID da biblioteca.

    Returns:
        HttpResponse: A resposta HTTP renderizada contendo a lista de livros da biblioteca especificada.
    """
    livros = Book.objects.filter(library=biblioteca_id)
    return render(request, 'pages/livros.html', {'livros': livros, 'biblioteca_id': biblioteca_id})

def graficos(request):
    """
    Renderiza a página de gráficos.

    Esta função também obtém dados sobre a contagem de livros cadastrados por mês e o número total de livros em cada biblioteca.

    Args:
        request (HttpRequest): O objeto HttpRequest que representa a requisição HTTP.

    Returns:
        HttpResponse: A resposta HTTP renderizada contendo os gráficos e dados relevantes.
    """
    six_months_ago = datetime.now() - timedelta(days=30*6)
    books_per_month = Book.objects.filter(creation_date__gte=six_months_ago).extra({'month': "EXTRACT(month FROM creation_date)"}).values('month').annotate(count=Count('id'))

    libraries = Library.objects.all()

    context = {
        'books_per_month': books_per_month,
        'libraries': libraries,
    }

    return render(request, 'pages/graficos.html', context)
