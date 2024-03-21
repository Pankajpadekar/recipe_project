from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from .models import *

# Create your views here.


def home(request):
    return render(request, 'home.html')


def receipes(request):
    if request.method == "POST":
        data = request.POST
        receipe_name = data.get('receipe_name')
        receipe_description = data.get('receipe_description')
        receipe_image = request.FILES['receipe_image']

        Receipe.objects.create(receipe_name=receipe_name,
                               receipe_description=receipe_description,
                               receipe_image=receipe_image)

        return redirect('/receipes/')

    receipes = Receipe.objects.all()
    template = loader.get_template('receipes.html')
    context = {
        'receipes': receipes,
    }

    return HttpResponse(template.render(context, request))


def delete_receipe(request, id):
    receipes = Receipe.objects.get(id=id)
    receipes.delete()
    return redirect('/receipes/')


def update_receipe(request, id):
    receipes = Receipe.objects.get(id=id)

    if request.method == "POST":
        data = request.POST
        receipe_name = data.get('receipe_name')
        receipe_description = data.get('receipe_description')
        receipe_image = request.FILES['receipe_image']

        Receipe.objects.create(receipe_name=receipe_name,
                               receipe_description=receipe_description)

        if receipe_image:
            receipes.receipe_image = receipe_image

        receipes.save()

    template = loader.get_template('update_receipes.html')
    context = {
        'receipes': receipes,
    }
    return HttpResponse(template.render(context, request))
