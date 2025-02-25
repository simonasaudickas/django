from django.shortcuts import render
from django.http import HttpResponse
from .forms import StudentForm, ContactForm
from django.core.mail import EmailMessage

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

def success(request):
    return render(request, 'sekmingai_parasyta.html')
def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message'] + "  "+ form.cleaned_data['phone']
            subject= form.cleaned_data['subject']


            EmailMessage(
               '{} Žinutė iš kontaktų formos nuo {}'.format(name, subject),
               message,
               'info@teipsiko.lt', # Send from (your website)
               ['teipsiko@gmail.com'], # Send to (your admin email)
               [],
               reply_to=[email] # Email from the form to get back to
           ).send()

            return render(request, 'sekmingai_parasyta.html')
    else:
        form = ContactForm()
    return render(request, 'susisiekti.html', {'form': form})
