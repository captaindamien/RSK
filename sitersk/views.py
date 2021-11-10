from django.shortcuts import render
from .models import Parent, Category, News
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def side_menu():
    menu = []
    parents = Parent.objects.all()

    for parent in parents:
        if parent.is_avaliable is True:
            menu.append({'name': parent.name,
                         'url_name': parent.link,
                         })
    return menu


def index(request):
    menu = side_menu()
    text = Category.objects.get(parent__link="index")
    content = {'menu': menu,
               'text': text,
               }
    return render(request, 'index.html', content)


def disclosure(request):
    menu = side_menu()
    category = Category.objects.filter(parent__link="disclosure")
    news = News.objects.filter(category__in=category)
    content = {'menu': menu,
               'category': category,
               'news': news,
               }
    return render(request, 'disclosure.html', content)


def news(request, pk):
    menu = side_menu()
    news = News.objects.get(pk=pk)
    content = {'menu': menu,
               'news': news,
               }
    return render(request, 'news.html', content)


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

    content = {'menu': menu,
               'posts': posts,
               'page': page,
               }
    return render(request, 'category_news.html', content)
