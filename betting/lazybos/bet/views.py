from django.shortcuts import render
from django.http import HttpResponse
from .forms import StudentForm

# Create your views here.
def index(request):
    return render(request, 'index.html')
def say_hello(request):
    return render(request, 'main.html', {"name":"mygtukas"})

def simple_form(request, methods=['GET', 'POST']):
    form = StudentForm()
    if request.method == 'POST':
        print(request.POST)
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
    context = {'form': form}
    return render (request, 'simple_form.html', context)

def komanda(request, methods = ['GET', 'POST']):
    return render(request,'komanda.html')

def article(request):
    context = {}
    return render(request, 'article/straipsniai.html', context)

def test(request):
    return render(request, 'testing_java.html')