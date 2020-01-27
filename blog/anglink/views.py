from django.shortcuts import render,HttpResponse,redirect
from . forms import *
from . models import userr
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt    

# Create your views here.
def view_userr(request):
    p = userr.objects.all().values('id','name','age','address')
    json_result = json.dumps(list(p))
    return HttpResponse(json_result,content_type='json')

    
def add_userr(request):
    if(request.method == 'GET'):
        form = NewUserForm()
        return render(request,'adduserr.html',{'form':form})
    else:
        form=NewUserForm(request.POST)
        if(form.is_valid()):
            # form.save()
            # return HttpResponse("New Item Added")
            pr=userr(**form.cleaned_data)
            pr.save()
            # return HttpResponse("New Item Added")
            return HttpResponse('success')
        else:
            return render(request,'adduserr.html',{'form':form})
def edit_userr(request,pid):
    # id = request.GET['pid']
    # # return render(request,'edit.html',{"data":id})                
    item = userr.objects.get(id=pid)
    if (request.method == 'GET'):
        form = MNewUserForm(instance=item)
        return render(request,'edit1.html',{'form':form})
    else:
        form=MNewUserForm(request.POST,instance=item)
        print(request.POST)
        if form.is_valid():
            form.save()
            # pr=products(**form.cleaned_data)
            # pr.save()
            # return HttpResponse("New Item Added")
            return redirect("view_userr")
        else:
            return render(request,'edit1.html',{'form':form})

def delete_userr(request,pid):
    item = userr.objects.get(id=pid)
    item.delete()
    return HttpResponse('deleted')

@csrf_exempt
def add_new_userr(request):
    response = {
        'status':'success',
        'errors':None,
    }
    print(json.loads(request.body))
    np = NewUser(json.loads(request.body))
    print(json.loads(request.body))
    if(np.is_valid()):
        print("saving data")
        np.save()
        return JsonResponse(response)
    else:
        response['status']='failed'
        response['error']=np.errors
        return JsonResponse(response)
