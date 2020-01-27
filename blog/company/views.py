from django.shortcuts import render,HttpResponse,redirect
from . forms import MEmployeeForm,EmployeeForm,EmployeeLogin
from . models import employee
from django.core.files.storage import FileSystemStorage
from .forms import DocumentForm
c=''
# Create your views here.
def add_empolyee(request):
    if(request.method == 'GET'):
        form = EmployeeForm()
        return render(request,'add-employee.html',{'form':form})
    else:
        form=EmployeeForm(request.POST)
        if(form.is_valid()):
            # form.save()
            # return HttpResponse("New Item Added")
            pr=employee(**form.cleaned_data)
            pr.save()
            # return HttpResponse("New Item Added")
            return redirect("https://www.google.com/",permanent=False)
        else:
            return render(request,'add-employee.html',{'form':form})
def login_employee(request):
    if(request.method == 'GET'):
        form = EmployeeLogin()
        return render(request,'add-employee.html',{'form':form})
    else:
        usrname = request.POST['username']
        pwrd = request.POST['password']
        global c
        c = employee.objects.filter(username=usrname,password=pwrd)
        if c:
            request.session['login']='admin'
            if request.session.has_key('login'):
                # return render(request,'profile.html',{'data':c})
                return redirect('dashboard',permanent=False)
                
        else:
            return HttpResponse('Invalid')
def dashboard(request):
    if not request.session.has_key('login'):
        return redirect('empolyee-login',permanent=False)
    else:
        return render(request,'profile.html',{'data':c})

def emp_logout(request):
    if request.session.has_key('login'):
        del request.session['login']
    return redirect('empolyee-login',permanent=False)

def setcookie(request):
    resp = render(request,'profile.html')
    resp.ser_cookie('test',request.META['REMOTE_ADDR'])
    return resp

def getcookie(request):
    return HttpResponse(request.COOKIES.get('test'))

def upload(request):
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name,myfile)
        uploaded_file_url = fs.url(filename)
        return render(request,'upload.html',{
            'uploaded_file_url':uploaded_file_url
        })
    else:
        return render(request,'upload.html')
def mupload(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST,request.FILES)
        if (form.is_valid()):
            form.save() 
            return redirect('https://www.google.com/')
    else:
        form = DocumentForm()
        return render(request,'mupload.html',{'form':form})
