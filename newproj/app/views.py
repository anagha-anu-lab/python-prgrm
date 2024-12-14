from django.shortcuts import render

# Create your views here.
def ab(request):
    return render(request,"home.html")