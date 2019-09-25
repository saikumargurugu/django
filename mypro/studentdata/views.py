from django.shortcuts import render, redirect
from .models import det
from django.views.decorators.csrf import csrf_protect
from django.contrib import messages
from django.http import HttpResponse
def home(request):
    s={
        'det': det.objects.all()
    }

    return render(request,"see/home.html",s)

def adddata(request):
    if request.method == 'POST':
        print("dine1")
        post=det()
        post.name= request.POST.get('name')
        e=post.email= request.POST.get('email')
        p=post.phno= request.POST.get('phno')
        result= e.find('@')
        if result >= 1:
            result=e.find('.')
            if  result >= 1:
                if len(p) == 10: 
                    if det.objects.filter(phno=p).exists():
                        messages.error(request, f'phno {p} is alredy used by some one else')
                        return render(request,'see/add.html')
                    if det.objects.filter(email=e).exists():
                        messages.error(request, f'email {e} is alredy used by some one else')
                        return render(request,'see/add.html')              
                    else:
                        post.save()
                        print("done")
                        return redirect('/home')
                else:
                    messages.error(request, f'error at phno lenth must be 10 @')
                    return render(request,'see/add.html')        
            else:
                messages.error(request, f'errror at email domail .com')
                return render(request,'see/add.html')
        else:
            messages.error(request, f'errror at email domail @')
            return render(request,'see/add.html')
    else:
         return render(request,'see/add.html')

def delet(request, id):
    print("hi")
    a=det()
    id=request.GET["id"]
    print("sas",id)
    a.delet(id)
    return redirect('/home')
