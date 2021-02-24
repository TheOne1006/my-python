from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.
# 1.路由配置  2. HttpResponse
def hello_world(request):
    # 需要使用  http response 实例
    return HttpResponse('Hello World')