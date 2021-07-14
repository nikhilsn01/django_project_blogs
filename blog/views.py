from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse('<h1>Home page blog</h1>')

def about(request):
    return HttpResponse('<h1>About page blog from nikhil S N</h1>')