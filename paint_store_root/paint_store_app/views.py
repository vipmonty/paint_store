from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, 'paint_store_app/index.html')
