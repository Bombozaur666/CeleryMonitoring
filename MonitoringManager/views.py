from django.shortcuts import render
# Create your views here.

def HomeView(reqest):
    return render(reqest, 'main.html')