from django.shortcuts import render
from rango.models import Category

from django.http import HttpResponse

def index(request):
    category_list = Category.objects.order_by('-likes')[:5]
    context_dict = {'categories': category_list}
    return render(request, 'rango/index.html', context=context_dict)

    #return HttpResponse("Rango says hey there partner! <br/> <a href='/rango/about/'>About</a>")

def about(request):
     context_dict = {'boldmessage': "ABOUT!"}
     return render(request, 'rango/about.html', context=context_dict)

     #return HttpResponse("Rango says here is the about page. <br/> <a href='/rango/'>Index</a>")
