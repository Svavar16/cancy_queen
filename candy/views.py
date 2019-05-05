from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
candies = [
    {
        'name': 'skitles',
        'price': 4.99
    },
    {
        'name': 'smarties',
        'price': 5.99
    }
]


def index(request):
    context = {'candies': candies}
    return render(request, 'candy/index.html', context)