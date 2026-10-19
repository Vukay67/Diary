from django.shortcuts import render 
from .models import Day

def main_page(request):
    day = Day.objects.all()
    
    context = {
        "day": day,
    }
    
    return render(request, 'index.html', context)