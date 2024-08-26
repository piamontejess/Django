from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import studentForm
from .models import student
from django.core.exceptions import ValidationError
import os
from django.conf import settings

def index(request):
    students = student.objects.all()
    if request.method == 'POST':
        form = studentForm(request.POST, request.FILES)
        if form.is_valid():
            try:
              
                if student.objects.filter(emailAdd=form.cleaned_data['emailAdd']).exists():
                    raise ValidationError('This email address is already taken.')
                
                
                if 'image' in request.FILES:
                    image = request.FILES['image']
                    image_path = os.path.join(settings.MEDIA_ROOT, "images", image.name)
                    with open(image_path, "wb") as f:
                        for chunk in image.chunks():
                            f.write(chunk)
                form.save()
                return redirect('index')
            
            except ValidationError as e:
                form.add_error('emailAdd', e)
                return HttpResponse(e)
        else:
            return HttpResponse(form.errors.items())
    else:
        form = studentForm()
    return render(request, 'index.html', {'students': students})

def view_students(request):
    students = student.objects.all()
    return render(request, 'index.html', {'students': students})
