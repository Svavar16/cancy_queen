from django.shortcuts import render, get_object_or_404, redirect
from candy.models import Candy, CandyImage
from candy.forms.candy_form import CandyCreateForm

# Create your views here.


def index(request):
    context = {'candies': Candy.objects.all().order_by('name')}
    return render(request, 'candy/index.html', context)


def get_candy_by_id(request, id):
    render(request, 'candy/candy_details.html', {
        'candy': get_object_or_404(Candy, pk=id)
    })


def create_candy(request):
    if request.method == 'POST':
        form = CandyCreateForm(data=request.POST)
        if form.is_valid():
            candy = form.save()
            candy_image = CandyImage(image=request.POST['image'], candy=candy)
            candy_image.save()
            return redirect()
    else:
        form = CandyCreateForm()
    return render(request, 'candy/create_candy.html', {
        'form': form
    })