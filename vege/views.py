from django.shortcuts import render
from .models import *

# Create your views here.


def receipes(request):
    if request.method == "POST":
        data = request.POST
        receipe_name = data.get('receipe_name')
        receipe_description = data.get('receipe_description')
        receipe_image = request.FILES['receipe_image']

        Receipe.objects.create(receipe_name=receipe_name,
                               receipe_description=receipe_description,
                               receipe_image=receipe_image)
    return render(request, 'receipes.html')
