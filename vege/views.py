from django.shortcuts import render, redirect
from .models import Receipe
# Create your views here.


def home(request):
    if request.method == "POST":
        data = request.POST
        receip_name = data.get('receipe_name')
        receipe_description = data.get('receipe_description')
        receipe_image = request.FILES.get("receipe_image")

        Receipe.objects.create(
            receipe_name = receip_name,
            receipe_desc = receipe_description,
            receipe_image = receipe_image
        )
        return redirect('home')
    return render(request, 'index.html')

def receipes(request):
    data = Receipe.objects.all()
    
    if request.GET.get('search'):
        data = data.filter(receipe_name__icontains = request.GET.get('search'))

    return render(request, 'receipe.html', context={'receipe': data})

def delete_receipes(request, id):
    data = Receipe.objects.get(id=id)
    data.delete()
    return redirect('receipes')

def update_receipes(request, id):
    data = Receipe.objects.get(id=id)
    context = {'receipe': data}
    if request.method == "POST":
        data2 = request.POST
        data.receipe_name = data2.get('receipe_name')
        data.receipe_desc = data2.get('receipe_description')
        if request.FILES.get("receipe_image"):
            data.receipe_image = request.FILES.get("receipe_image")
        data.save()
        return redirect('receipes')
        
    return render(request, 'update_receipe.html', context=context)