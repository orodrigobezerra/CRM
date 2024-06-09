from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def create_lead(request):
  return render(request, 'leads/create_lead.html')

@login_required
def read_lead(request):
  return render(request, 'leads/read_lead.html')

@login_required
def update_lead(request):
  return render(request, 'leads/update_lead.html')

@login_required
def delete_lead(request):
  return render(request, 'leads/delete_lead.html')
