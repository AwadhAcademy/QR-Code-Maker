from django.shortcuts import render
from .models import code_data
from django.core.files.base import ContentFile
import qrcode
# Create your views here.


def home(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        data = request.POST.get('data')
        image = qrcode.make(data)
        image.save(f"{name} .png")
        data = code_data(name=name, data=data)
        data.save()
    return render(request, "code_gen/basic.html")


def code(request):
    return render(request, 'code_gen/code.html')
