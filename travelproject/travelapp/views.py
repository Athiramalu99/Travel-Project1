from django.shortcuts import render
from .models import Places, Team


# Create your views here.
def demo(request):
    obj = Places.objects.all()
    team = Team.objects.all()
    return render(request, "index.html", {'result': obj, 'team': team})
