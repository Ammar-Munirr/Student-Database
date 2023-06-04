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