from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .models import Users

def register(request):
  if request.method == 'POST':
    form = UserCreationForm(request.POST)

    if form.is_valid():
      user = form.save()
      Users.objects.create(user=user)

      return redirect('/login/')
    
  else:
    form = UserCreationForm()

  form = UserCreationForm

  return render(request, 'user/register', {
    'form': form
  })