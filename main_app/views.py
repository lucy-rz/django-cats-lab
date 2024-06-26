from django.shortcuts import render, redirect
from .models import Cat
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .forms import FeedingForm



# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def cats_index(request):
    cats = Cat.objects.all()
    return render (request, 'cats/index.html', {
        'cats': cats
    })
def cats_detail(request, cat_id):
    #to communicate with the db here
    cat = Cat.objects.get(id=cat_id)
    feeding_form = FeedingForm()
    return render(request, 'cats/detail.html', {
        'cat': cat,
        'feeding_form': feeding_form
    })

def add_feeding(request, cat_id):
    submitted_form = FeedingForm(request.POST) #creates django version of req.body
    if submitted_form.is_valid():
        new_feeding = submitted_form.save(commit=False) #commit=false ensures it doesn't submit to db
        new_feeding.cat_id = cat_id
        new_feeding.save()
    return redirect('detail', cat_id=cat_id)


class CatCreate(CreateView):
    model = Cat
    fields = '__all__'

class CatUpdate(UpdateView):
    model = Cat
    fields = ('description', 'age')

class CatDelete(DeleteView):
    model = Cat
    success_url = '/cats/'