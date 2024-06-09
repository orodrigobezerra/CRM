from django import forms
from . import models

class CreateLeadForm(forms.ModelForm):
  class Meta:
    model = Leads
    fields = ('name', 'email', 'description', 'priority', 'status')