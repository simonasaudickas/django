from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

from .forms import CreateUserForm, CreateArticleForm
from django.contrib.auth.decorators import login_required


# Create your views here.
def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect('profilis')
        else:
            messages.info(request, 'Prisijungimo duomenys neteisingi')
            return redirect('login')
    return render (request, 'authenticate/login.html', {})

@login_required(login_url ='login')
def logout_user(request):
    logout(request)
    return redirect('login')
def user_registration(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Paskyra buvo sekmingai sukurta ' + user)
            return redirect('login')


    context = {'form':form}
    return render(request, 'authenticate/register.html', context)

@login_required(login_url ='login')
def profilis(request):
    context= {}
    return render(request, 'authenticate/profile.html', context)

@login_required(login_url ='login')
def post_article(request):
    if request.method == 'POST':
        form = CreateArticleForm(request.POST)
        if form.is_valid():
            form.save()
            pavadinimas = form.cleaned_data.get('pavadinimas')
            messages.success(request, 'Straipsnis: ' + pavadinimas + ' buvo sėkmingai sukurtas')  # Corrected Lithuanian characters
            return redirect('login')
    else:
        form = CreateArticleForm()

    context = {'form': form}
    return render(request, 'article/submit_article.html', context)


"""
def my_view(request):
    
    if user is not None:
        if user.is_active:
            login(request, user)
            # Redirect to a success page.
        else:
            # Return a 'disabled account' error message
            ...
    else:
        # Return an 'invalid login' error message.
        ...

"""