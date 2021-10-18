from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .models import quiz

def home(request):

    return render(request, "index.html")
def next(request):
    if request.method=='POST':
        name=request.POST['name']
        ins=quiz(name=name)
        ins.save()
    return render(request, "question1.html")
def next2(request):
    if request.method=='POST':
        name=request.POST['name']
        ins=quiz(name=name)
        ins.save()
    return render(request, "question2.html")
def next3(request):
    if request.method=='POST':
        name=request.POST['name']
        ins=quiz(name=name)
        ins.save()
    return render(request, "summary.html")