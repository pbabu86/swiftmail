from django.shortcuts import render,HttpResponse,redirect
from messageapp.models import Msg


# Create your views here.
def create(request):
    #print("Request is:",request.method)
    if request.method=="GET":
        #print("In if section")
        return render(request,'create.html')
    
    else:
        #fetch data from the form
        n=request.POST['uname']
        mail=request.POST['uemail']
        mob=request.POST['mobile']
        msg=request.POST['msg']
        #validation
        #insert
        m=Msg.objects.create(name=n,email=mail,mobile=mob,msg=msg)
        m.save()
        return redirect('/dashboard')
        """
        print("Name:",n)
        print("mail:",mail)
        print("Mobile:",mob)
        print("Message:",msg)

        return HttpResponse("data fetched Successfully")
        """
        #return HttpResponse("data inserted Successfully")

def dashboard(request):
    m=Msg.objects.all()
    #print(m)
    context={}
    context['data']=m
    return render(request, 'dashboard.html',context)

def delete(request,rid):
   # print("ID to be deleted:",rid)
    #return HttpResponse("Id to be deleted:"+rid)
    m=Msg.objects.filter(id=rid)#fetch that object
    #print(m)
    m.delete()
    return redirect('/dashboard')

def edit(request,rid):
    #print("ID to be edited:",rid)
    #return HttpResponse("Id to be edited:"+rid)
    if request.method=="GET":
        m=Msg.objects.filter(id=rid)
        #print(m)
        context={}
        context['data']=m
        return render(request,'edit.html',context)
    else:
        #pass
        upname=request.POST['uname']
        upemail=request.POST['uemail']
        upmob=request.POST['mobile']
        upmsg=request.POST['msg']
        #print(upname)
        #print(upemail)
        #print(upmob)
        #print(upmsg)
        m=Msg.objects.filter(id=rid)
        m.update(name=upname,email=upemail,mobile=upmob,msg=upmsg)
        #return HttpResponse("Data is fetched")
        return redirect('/dashboard')
    
    
    


