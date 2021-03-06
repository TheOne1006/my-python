from django.shortcuts import render

from django.http import HttpResponse
from blog.models import Article

# Create your views here.
# 1.路由配置  2. HttpResponse
def hello_world(request):
    # 需要使用  http response 实例
    return HttpResponse('Hello World')


def article_content(request):
    article = Article.objects.all()[0]
    title = article.title
    content = article.content
    article_id = article.article_Id
    s = 'title: %s, content: %s, article_id: %s' % (title, content, article_id)
    return HttpResponse(s)


def get_index_page(request):
    articles = Article.objects.all()
    return render(request, 'index.html', {
        'article_list': articles,
    })

def get_detail_page(request, id):
    articles = Article.objects.all()

    return render(request, 'detail.html', {
        'article': articles[id - 1],
    })