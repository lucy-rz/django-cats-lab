from django.shortcuts import render

#Temporary db - REMOVE THIS AFTER ADDING CAT MODEL
cats = [
    {'name': 'Garfield', 'breed': 'fluffy', 'description': 'orange', 'age': '43'},
    {'name': 'Grumpy', 'breed': 'mix', 'description': 'grumpy', 'age': '7'},
]

# Create your views here.
def home(request):
    return render(request, 'home.html')

# add a new view function 'about', to render about.html
def about(request):
    return render(request, 'about.html')

def cats_index(request):
    return render (request, 'cats/index.html', {
        'cats': cats,
    })