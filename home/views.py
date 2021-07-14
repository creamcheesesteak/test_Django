from urllib import request

from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def index(request):
    path = request.path
    resultstr = ''
    if path == '/home':
        resultstr = '<h1>여기는 home입니다</h1>'
    else :
        resultstr = '<h1>여기는 master입니다</h1>'


    return HttpResponse(resultstr)

def index01(ruquest):
    result = {'first':'taehyeok', 'second':'im'}
    return render(request, 'index.html', context=result)

def index02(ruquest):
    # request.GET['']
    result = {'first':request.GET['taehyeok'], 'second':request.GET['im']}
    return render(request, 'index.html', context=result)