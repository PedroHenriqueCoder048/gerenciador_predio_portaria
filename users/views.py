from django.shortcuts import render

def home_user(request):
    return render(request,'users/index.html')