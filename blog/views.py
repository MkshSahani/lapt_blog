from django.shortcuts import render

def home_page(request): 
    context = {}

    return render(request, 'main_blog.html', context)
    