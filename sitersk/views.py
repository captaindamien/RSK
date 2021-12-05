from django.shortcuts import render
from .models import Parent, Category, News, UploadFile
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def side_menu():
    menu = []
    parents = Parent.objects.all()

    for parent in parents:
        if parent.is_avaliable is True:
            menu.append(
                {
                    'name': parent.name,
                    'url_name': parent.link,
                }
            )
    return menu


def index(request):
    menu = side_menu()
    category = Category.objects.get(parent__link="index")

    try:
        text = News.objects.get(category__pk=category.pk)
    except Exception as e:
        text = e

    context = {
        'menu': menu,
        'text': text,
    }
    return render(request, 'index.html', context)


def disclosure(request):
    menu = side_menu()
    category = Category.objects.filter(parent__link="disclosure")

    context = {
        'menu': menu,
        'category': category,
    }
    return render(request, 'disclosure.html', context)


def news(request, pk):
    menu = side_menu()
    news = News.objects.get(pk=pk)
    files = UploadFile.objects.filter(news__name=news)

    context = {
        'menu': menu,
        'news': news,
        'files': files,
    }
    return render(request, 'news.html', context)


def category_news(request, pk):
    menu = side_menu()
    news = News.objects.filter(category__id=pk)
    paginator = Paginator(news, 5)
    page = request.GET.get('page')

    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    context = {
        'menu': menu,
        'posts': posts,
        'page': page,
    }
    return render(request, 'category_news.html', context)


def contacts(request):
    menu = side_menu()
    category = Category.objects.get(parent__link="contacts")

    try:
        text = News.objects.get(category__pk=category.pk)
    except Exception as e:
        text = e

    context = {
        'menu': menu,
        'text': text,
    }
    return render(request, 'index.html', context)
