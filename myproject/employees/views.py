from django.shortcuts import render,HttpResponse
from . forms import Login as LoginForm

# Create your views here.
def home(request):
    return HttpResponse("hi welcome")
def Login(request):
    if(request.method=='GET'):
        form= LoginForm()
        return render(request,'login.html',{"form":form})
    else:
        form = LoginForm(request.POST)
        if(form.is_valid()):
            return HttpResponse("ok")
        else:
            return render(request,'login.html',{"form":form})