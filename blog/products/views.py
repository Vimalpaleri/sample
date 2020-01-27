from django.shortcuts import render,HttpResponse,redirect
from . forms import MNewProductForm,NewProductForm
from . models import products


    

# Create your views here.
def view_products(request):
    #select *
    p = products.objects.all()
    # #select with where
    # p = products.objects.filter(name= 'iphone')
    # #reverse order (sort by python)
    # p = products.objects.all().order_by('name')[::-1]
    # #reverse order (sort using database)
    # p = products.objects.all().order_by('-name')
    return render(request,'product_1.html',{'data':p})
def product(request):
    return render(request,"products.html")
def add_product(request):
    if(request.method == 'GET'):
        form = NewProductForm()
        return render(request,'addproduct.html',{'form':form})
    else:
        form=NewProductForm(request.POST)
        if(form.is_valid()):
            # form.save()
            # return HttpResponse("New Item Added")
            pr=products(**form.cleaned_data)
            pr.save()
            # return HttpResponse("New Item Added")
            return redirect("https://www.google.com/",permanent=False)
        else:
            return render(request,'addproduct.html',{'form':form})
def edit_product(request,pid):
    # id = request.GET['pid']
    # # return render(request,'edit.html',{"data":id})                
    item = products.objects.get(id=pid)
    if (request.method == 'GET'):
        form = MNewProductForm(instance=item)
        return render(request,'edit.html',{'form':form})
    else:
        form=MNewProductForm(request.POST,instance=item)
        print(request.POST)
        if form.is_valid():
            form.save()
            # pr=products(**form.cleaned_data)
            # pr.save()
            # return HttpResponse("New Item Added")
            return redirect("view_products")
        else:
            return render(request,'edit.html',{'form':form})

def delete_product(request,pid):
    item = products.objects.get(id=pid)
    item.delete()
    return HttpResponse('deleted')
