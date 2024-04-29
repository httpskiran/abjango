from django.shortcuts import render

# Create your views here.
def home (request):
    return render(request,'home.html')
def login (requestlogin):
    return render(requestlogin,'login.html')