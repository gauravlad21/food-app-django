from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.contrib import messages


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Welcome {username}')
            return redirect('login')
    else:  # get
        form = RegisterForm()
    return render(request, 'users/register.html', {'form': form})
