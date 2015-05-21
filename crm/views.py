from django.shortcuts import render

# Create your views here.

def index(request):
    age = 12
    name = 'liming'
    return render(request, 'index.html', locals())