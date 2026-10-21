import os

from django.contrib import messages
from django.db.models import Q
from django.http import Http404
from django.shortcuts import get_list_or_404, get_object_or_404, render

from utils.pagination import make_pagination

from .models import Recipe

PER_PAGES = os.environ.get('PER_PAGE', '6')


def home(request):
    recipes = Recipe.objects.filter(
                is_published=True
            ).order_by('-id')

    messages.success(request, 'TESTANDO FLASH MENSAGE DJANGO')
    
    page_object, pagination_range = make_pagination(request, recipes, PER_PAGES)

    return render(request, "recipes/pages/home.html", context={
        'recipes': page_object,
        'pagination_range': pagination_range
    })

def category(request, category_id):
    recipes = get_list_or_404(
        Recipe.objects.filter(
            category__id=category_id,
            is_published=True
        ).order_by('-id')
    )

    page_object, pagination_range = make_pagination(request, recipes, PER_PAGES)

    return render(request, "recipes/pages/category.html", context={
        'recipes': page_object,
        'pagination_range': pagination_range,
        'title': f'{recipes[0].category.name} - Category | ' #list
    })

def recipes(request, id):
    recipe = get_object_or_404(Recipe, pk=id, is_published=True)

    return render(request, "recipes/pages/recipe-view.html", context={
        'recipe': recipe,
        'is_detail_page': True,
    })

def search(request):
    search_term = request.GET.get('q', '').strip() # Isso é o que o usuário digitou na barra de pesquisa

    if not search_term:
        raise Http404()

    recipes = Recipe.objects.filter(
        Q(
            Q(title__icontains=search_term) | 
            Q(description__icontains=search_term),
        ),
        is_published=True
    ).order_by('-id')

    page_object, pagination_range = make_pagination(request, recipes, PER_PAGES)

    return render(request, "recipes/pages/search.html", context={
        'page_title': f'Pesquisa por "{search_term}" | ',
        'search_term': search_term,
        'recipes': page_object,
        'pagination_range': pagination_range,
        'additional_url_query': f'&q={search_term}'
    })

