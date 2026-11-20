from django.shortcuts import render

def book_cover(request):
    return render(request, 'book_cover.html')