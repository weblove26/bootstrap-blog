from django.shortcuts import render
from django.http import HttpResponse
from .models import Article
from django.core.paginator import Paginator


# Create your views here.
def lst(request):
    return HttpResponse('Hello World')


# 视图函数
def article_content(request):
    article = Article.objects.all()[0]
    article_id = article.article_id
    title = article.title
    brief_content = article.brief_content
    content = article.content
    publish_date = article.date
    return_str = 'article_id:%s,title:%s,brief_content:%s,' \
                 'content:%s,publish_date:%s' % (article_id, title,
                                                 brief_content, content,
                                                 publish_date)
    return HttpResponse(return_str)


def get_index_page(request):
    page = request.GET.get('page')
    if page:
        page = int(page)
    else:
        page = 1
    all_article = Article.objects.all()
    top5_article_list = Article.objects.order_by('-date')[:5]
    paginator = Paginator(all_article, 8)

    page_num = paginator.num_pages
    page_article_list = paginator.page(page)
    if page_article_list.has_next():
        next_page = page + 1
    else:
        next_page = page
    if page_article_list.has_previous():
        previous_page = page - 1
    else:
        previous_page = page
    return render(request, 'index.html',
                  {
                      'article_list': page_article_list,
                      'page_num': range(1, page_num + 1),
                      'curr_page': page,
                      'next_page': next_page,
                      'previous': previous_page,
                      'top5_article_list': top5_article_list,
                      'page': page
                  })


def get_detail_page(request, article_id):
    all_article = Article.objects.all()    
    top5_article_list = Article.objects.order_by('-date')[:5]
    print(type(all_article))
    print(all_article)
    curr_article = None
    previous_index = 0
    next_index = 0
    previous_article = None
    next_article = None
    for index, article in enumerate(all_article):
        if index == 0:
            previous_index = 0
            next_index = index + 1
        elif index == len(all_article) - 1:
            previous_index = index - 1
            next_index = index
        else:
            previous_index = index - 1
            next_index = index + 1
        if article.article_id == article_id:
            curr_article = article
            previous_article = all_article[previous_index]
            next_article = all_article[next_index]
            break
    section_list = curr_article.content.split('\n')
    return render(request, 'detail.html', {
        'curr_article': curr_article,
        'section_list': section_list,
        'previous_article': previous_article,
        'next_article': next_article,        
        'top5_article_list': top5_article_list
    })
