from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home_view(request, *args, **kwargs):
    return render(request, 'home.html', {} )

def about_view(request,*args, **kwargs):
    my_context = {
        "my_text": "this is about us",
        "my_number": 123,
        "my_list" : [123,456,789]
    }
    return render(request, 'about.html', my_context )

def blog_view(request, *args, **kwargs):
    return render(request, 'blog.html', {} )

def contact_view(request, *args, **kwargs):
    return render(request, "contact.html", {} )

def product_view(request, *args, **kwargs):
    return render(request, "product.html", {} )


