from django.shortcuts import render
API_KEY = 'API KEY HERE I HAD TOLD IN THE VIDEO HOW TO GET ONE'
# Create your views here.
import requests
def index(request):
    url = f'https://newsapi.org/v2/top-headlines?country=in&apiKey={API_KEY}'
    data = requests.get(url)
    response = data.json()
    articles = response['articles']
    context = {'articles':articles}
    return render(request,'index.html',context)

def category(request,name):
    url = f'https://newsapi.org/v2/top-headlines?category={name}&apiKey={API_KEY}'
    data = requests.get(url)
    response = data.json()
    articles = response['articles']
    context = {'articles':articles,'category':name}
    return render(request,'category.html',context)

def search(request):
    search_term = request.GET['search']
    url = f'https://newsapi.org/v2/everything?q={search_term}&apiKey={API_KEY}'
    data = requests.get(url)
    response = data.json()
    articles = response['articles']
    context = {'articles':articles,'search':search_term}
    return render(request,'search.html',context)
