#from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from .models import Student
from .forms import StudentCreate
from django.http import HttpResponse


def index(request):
    shelf = Student.objects.all()
    return render(request, 'student/base.html', {'shelf': shelf})

def upload(request):
    upload = StudentCreate()
    if request.method == 'POST':
        upload = StudentCreate(request.POST, request.FILES)
        if upload.is_valid():
            upload.save()
            return redirect('index')
        else:
            return HttpResponse("""your form is wrong, reload on <a href = "{{ url : 'index'}}">reload</a>""")
    else:
        return render(request, 'student/upload_form.html', {'upload_form':upload})

def update_student(request, roll):
    roll = int(roll)
    try:
        book_sel = Student.objects.get(id = roll)
    except Student.DoesNotExist:
        return redirect('index')
    book_form = StudentCreate(request.POST or None, instance = book_sel)
    if book_form.is_valid():
       book_form.save()
       return redirect('index')
    return render(request, 'student/upload_form.html', {'upload_form':book_form})

def delete_student(request, roll):
    roll = int(roll)
    # try:
    book_sel = Student.objects.get(id = roll)
    # except Student.DoesNotExist:
    book_sel.delete()
    return redirect('index')
    # return redirect('index')

