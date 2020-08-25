from django.shortcuts import render, HttpResponseRedirect, reverse
from django.contrib.auth import login, logout, authenticate

from .models import CustomUser
from .forms import LoginForm, SignupForm
from microscope_config.settings import AUTH_USER_MODEL

def home_view(request):
  return render(request, 'home.html', {'authcustomuser': AUTH_USER_MODEL})


def login_view(request):
  if request.method == 'POST':
    form = LoginForm(request.POST)
    if form.is_valid():
      data = form.cleaned_data
      user = authenticate(request, username=data.get('username'), password=data.get('password'))
      if user:
        login(request, user)
        return HttpResponseRedirect(request.GET.get('next', reverse('home')))
  form = LoginForm()
  return render(request, 'login.html', {'form': form})


def logout_view(request):
  logout(request)
  return HttpResponseRedirect(reverse('home'))


def signup_view(request):
  if request.method == "POST":
    form = SignupForm(request.POST)
    if form.is_valid():
      data = form.cleaned_data
      new_user = CustomUser.objects.create_user(
        username=data.get('username'),
        password=data.get('password'),
        age=data.get('age'),
        display_name=data.get('display_name'),
      )
      login(request, new_user)
      return HttpResponseRedirect(reverse('home'))
  form = SignupForm()
  return render(request, 'signup.html', {'form': form})
