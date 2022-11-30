from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse('<h1>Hello World!/ᐠ｡‸｡ᐟ\ﾉ</h1>')

def about(request):
    return HttpResponse('<h1>I am Catherine the developer</h1>')

def contact(request):
    return HttpResponse('<h1>Hey, I just met you, this is crazy, here''s my number, call me maybe? 555-555-555</h1>')

def blog(request):
    return HttpResponse('<h1>This is my blog</h1>')

# Create your views here.
#similar to controllers in javascript...this is like an index file
