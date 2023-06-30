from django.shortcuts import render
from .models import Places


# Create your views here.
def demo(request):
    obj = Places.objects.all()

    return render(request, "index.html", {'result': obj})
