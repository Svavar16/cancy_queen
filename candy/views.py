from django.shortcuts import render
from candy.models import Candy

# Create your views here.


def index(request):
    context = {'candies': Candy.objects.all().order_by('name')}
    return render(request, 'candy/index.html', context)