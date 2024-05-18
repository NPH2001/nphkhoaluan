from django import forms

class MotifsamplerForm(forms.Form):
  file = forms.FileField(),
  output_m = forms.CharField(max_length=100),