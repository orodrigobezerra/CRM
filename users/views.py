from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .models import usersprofile

def register(request):
  if request.method == 'POST':
    form = UserCreationForm(request.POST)

    if form.is_valid():
      user = form.save()
      usersprofile.objects.create(user=user)

      return redirect('/login/')
    
  else:
    form = UserCreationForm()

  form = UserCreationForm

  return render(request, 'users/register.html', {
    'form': form
  })