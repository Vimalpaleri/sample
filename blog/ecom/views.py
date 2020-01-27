from django.shortcuts import render,HttpResponse,redirect
from . forms import *
from . models import category,prod

# Create your views here.
def add_category(request):
    if(request.method == 'GET'):
        form = Category()
        return render(request,'addcat.html',{'form':form})
    else:
        form=Category(request.POST,request.FILES)
        print(request.POST)  
        if(form.is_valid()):
            form.save()
            return HttpResponse("New Item Added")
            # pr=products(**form.cleaned_data)
            # pr.save()
        else:
            return render(request,'addcat.html',{'form':form})
def add_product(request):
    if(request.method == 'GET'):
        form = prodForm()
        return render(request,'addprod.html',{'form':form})
    else:
        form=prodForm(request.POST)
        if(form.is_valid()):
            form.save()
            return HttpResponse("New Item Added")
            # pr=products(**form.cleaned_data)
            # pr.save()
        else:
            return render(request,'addprod.html',{'form':form})

def mainEcom(request):
    f=category.objects.all()
    return render(request,'view_ecom.html',{'data':f})

def viewProd(request,pid):
    f=category.objects.filter(id=pid)[0]
    print(f)
    p = prod.objects.filter(categorys=f)
    print(p)
    return render(request,'view_prod.html',{'data':p})

