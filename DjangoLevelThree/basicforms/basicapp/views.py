from django.shortcuts import render
from . import forms
# Create your views here.

def index(request):
    return render(request, 'basicapp/index.html')

def form_name_view(request):
    form = forms.FormName()
    if form.is_valid():
        #DO SOMETHING
        print("Validation successful !! ")
        print("Name: " + form.cleaned_data['name'])
        print("Email: " + form.cleaned_data['email'])
        print("Text: " + form.cleaned_data['text'])

    return render(request, 'basicapp/form_page.html', {'form': form})