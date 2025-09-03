from django.shortcuts import render,HttpResponse,redirect
from .models import Student

# Create your views here.
def Home(request):
    return render(request, 'Home.html')


def send(request):
    if request.method == 'POST':
        ID = request.POST['ID']
        FirstName = request.POST['FirstName']
        LastName = request.POST['LastName']
        Gender = request.POST['Gender']
        Email = request.POST['Email']
        ContactNumber = request.POST['ContactNumber']
        Student(ID=ID,FirstName=FirstName,LastName=LastName,Gender=Gender,Email=Email,ContactNumber=ContactNumber).save()
        msg = 'Data Stored Successfully'
        return render(request, 'Home.html', {'msg':msg})
    else:
        return HttpResponse('<h1>404 - not found</h1>')
    

def Show(request):
    data = Student.objects.all()
    return render(request,'Show.html',{'data':data})


def delete(request):
    ID = request.GET.get('ID') 
    Student.objects.filter(ID=ID).delete()
    return redirect('Show')

def edit(request):
    ID=request.GET.get('ID')
    for data in Student.objects.filter(ID=ID):
        FirstName = data.FirstName
        LastName = data.LastName
        Gender = data.Gender
        Email = data.Email
        ContactNumber = data.ContactNumber
    return render(request,'edit.html',{'ID':ID,'FirstName':FirstName,'LastName':LastName,'Gender':Gender,'Email':Email,'ContactNumber':ContactNumber})

def reedit(request):
    if request.method == 'POST':
        ID = request.POST['ID']
        FirstName = request.POST['FirstName']
        LastName = request.POST['LastName']
        Gender = request.POST['Gender']
        Email = request.POST['Email']
        ContactNumber = request.POST['ContactNumber']
        Student.objects.filter(ID=ID).update(FirstName=FirstName,LastName=LastName,Gender=Gender,Email=Email,ContactNumber=ContactNumber)
        return redirect('Show')
    else:
        return HttpResponse("404 - not found")


