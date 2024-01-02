from django.shortcuts import render
from datetime import datetime

now = datetime.now()
day = now.day
month = now.month
year = now.year
specific_date = datetime(year, month, day)
day_of_week = specific_date.strftime('%A')


# Create your views here.
def index(request):
    return render(request,"day_app/index.html",{
        'day':day_of_week
    })