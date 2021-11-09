from django.shortcuts import render
from .models import Parent, Category, News
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

menu = [{'name': 'О компании', 'url_name': 'index'},
        {'name': 'Раскрытие информации', 'url_name': 'disclosure'}]


def index(request):
    text = Category.objects.get(name="Главная страница")
    content = {'menu': menu, 'text': text}
    return render(request, 'index.html', content)


def disclosure(request):
    category = Category.objects.filter(parent__name="Раскрытие информации")
    news = News.objects.filter(category__in=category)
    content = {'menu': menu, 'category': category, 'news': news}
    return render(request, 'disclosure.html', content)


def news(request, pk):
    news = News.objects.get(pk=pk)
    content = {'menu': menu, 'news': news}
    
    return render(request, 'news.html', content)


def category_news(request, pk):
    news = News.objects.filter(category__id=pk)
    paginator = Paginator(news, 5)
    page = request.GET.get('page')

    try:  
        posts = paginator.page(page)  
    except PageNotAnInteger:  
        posts = paginator.page(1)  
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    content = {'menu': menu, 'posts': posts, 'page': page}
    return render(request, 'category_news.html', content)