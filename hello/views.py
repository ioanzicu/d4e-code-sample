from django.http import request
from django.http.response import HttpResponse
from django.shortcuts import render

# Create your views here.


def myview(request):
    cookie_val = 'dj4e_cookie'
    val = int(request.COOKIES.get('count', 0)) + 1
    context = {
        'views_count': f'view count={val}'
    }
    resp = render(request, 'hello/main.html', context)
    resp.set_cookie(cookie_val, 'ba074519', max_age=1000)
    val = val if val < 4 else 0
    resp.set_cookie('count', val)

    return resp
