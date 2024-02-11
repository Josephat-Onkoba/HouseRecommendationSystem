from django.shortcuts import render

# Create your views here.
def account_selector(request):
    return render(request,'home.html')