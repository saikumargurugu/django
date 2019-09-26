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
    print("sas",id)
    det.objects.filter(id=id).delete()
    return redirect('/home')

def update(request, id):
    s={
        'det': det.objects.filter(id=id)
    }
    if request.method == 'POST':
        print("dine1")
        post= det.objects.get(id=id)
        post.name= request.POST.get('name')
        e=post.email= request.POST.get('email')
        p=post.phno= request.POST.get('phno')
        if post.name:
            post.name= request.POST.get('name')
           
        if post.email:
            result= e.find('@')
            if result >= 1:
                result=e.find('.')
                if  result >= 1:
                    if det.objects.filter(email=e).exists():
                        messages.error(request, f'email {e} is alredy used by some one else')
                        return render(request,'see/update.html',s)  
                    else:
                        post.email= request.POST.get('email')
                        
                else:
                    messages.error(request, f'errror at email domail .com')
                    return render(request,'see/update.html',s)
            else:
                messages.error(request, f'errror at email domail @')
                return render(request,'see/update.html',s)
        if post.phno:
            if len(p) == 10: 
                if det.objects.filter(phno=p).exists():
                    messages.error(request, f'phno {p} is alredy used by some one else')
                    return render(request,'see/update.html',s)         
                else:
                    post.phno=request.POST.get('phno')
                    
                    
            else:
                messages.error(request, f'error at phno lenth must be 10 @')
                return render(request,'see/update.html',s)
        post.save()
        return redirect('/home')
                        
    else:
         return render(request,'see/update.html',s)
