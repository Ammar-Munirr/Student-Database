from django.shortcuts import render,redirect
from .models import Student
from django.contrib import messages
from .forms import StudentForm
import csv
import io
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

def import_csv(request):
    if request.method == 'POST' and request.FILES['csv_file']:
        csv_file = request.FILES['csv_file']
        if not csv_file.name.endswith('.csv'):
            messages.success(request,'Invalid CSV FILE')
            return redirect('/') 
        data_set = csv_file.read().decode('UTF-8')
        io_string = io.StringIO(data_set)
        next(io_string)
        for row in csv.reader(io_string, delimiter=',', quotechar="'"):
            print(row)
            name = row[0]
            age = row[1]
            email = row[2]
            password = row[3]
            Student.objects.create(name=name,age=age, email=email, password=password)
        return redirect('/')
    
    return render(request,'csv.html')

def export_csv(request):
    pass

def export_users_csv(request):
    pass