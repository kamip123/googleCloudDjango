from django.shortcuts import render

# Create your views here.


def ranking_page(request):
    return render(request, 'rankings.html')
