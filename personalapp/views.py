from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def personal_index(request):
    return render(request, 'personalapp/home.html')
