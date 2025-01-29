from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import LoginForm


def login_view(request: HttpRequest) -> HttpResponse:
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']

            user = authenticate(request, email=email, password=password)

            if user is not None:
                login(request, user)
                return render(request, 'users/success.html', {'email': email, 'password': password}) 

            form.add_error(None, 'Invalid email or password')

        return render(request, 'users/login.html', {'form': form})

    if request.user.is_authenticated:
        return render(request, 'users/success.html', {'email': request.user.email, 'password': request.user.password}) 

    return render(request, 'users/login.html', {'form': LoginForm()})
