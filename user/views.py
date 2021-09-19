from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .forms import UserRegistrationForm, UpdateDetails,UpdateProfile
from django.contrib import messages

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.info(request, f'Account creation for {username} succesful')
            return redirect('login')
    else:
        form = UserRegistrationForm()
    return render(request, 'user/register.html',{"form":form})


def profile(request):
    if request.method == 'POST':
        d_form = UpdateDetails(request.POST, instance=request.user)
        p_form = UpdateProfile(request.POST,request.FILES, instance=request.user.profile)
        if d_form.is_valid() and p_form.is_valid():
            d_form.save()
            p_form.save() 
            messages.info(request, 'Account Information Update succesful')
            return redirect('profile')
    else:
        d_form = UpdateDetails(instance=request.user)
        p_form = UpdateProfile(instance= request.user.profile)

    return render(request, 'user/profile.html',{"d_form":d_form,"p_form":p_form})
