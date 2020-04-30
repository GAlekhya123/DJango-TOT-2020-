from django.shortcuts import render,redirect
from django.http import HttpResponse
from myApp2.forms import StudentForm
from myApp2.models import Student
# Create your views here.
def hello(request):
	return HttpResponse('now ur in myApp2')

def register(request):
	if request.method=='POST':
		form = StudentForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('/myapp2/register')
	form = StudentForm()
	return render(request,'myApp2/register.html',{'form':form})

def details(request):
	data  = Student.objects.all()
	return render(request,'myApp2/datails.html',{'data':data})

def edit(request,id):
	data = Student.objects.get(id=id)
	if request.method=='POST':
		form = StudentForm(request.POST,instance=data)
		if form.is_valid():
			form.save()
			return redirect('/myapp2/details')
	form = StudentForm(instance=data)
	return render(request,'myApp2/edit.html',{'form':form,'data':data})







