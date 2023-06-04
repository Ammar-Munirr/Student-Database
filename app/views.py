from django.shortcuts import render,redirect
from .models import Student
from .forms import StudentForm
# Create your views here.
def add(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = StudentForm()
    data = Student.objects.all()
    return render(request,'add.html',{'form':form,'students':data})

def delete(request,id):
    data = Student.objects.get(id=id)
    data.delete()
    return redirect('/')


def edit(request,id):
    if request.method == 'POST':
        data = Student.objects.get(id=id)
        form = StudentForm(request.POST,instance=data)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        data = Student.objects.get(id=id)
        form = StudentForm(instance=data)
    return render(request,'edit.html',{'form':form})

def import_csv(requets):
    pass

def export_csv(request):
    pass

def export_users_csv(request):
    pass