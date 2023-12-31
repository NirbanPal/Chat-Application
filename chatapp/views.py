from django.contrib.auth  import login
from django.shortcuts import render,redirect
from .forms import SignUpFrom


# Create your views here.

def frontpage(request):
    return render(request,'chatapp/frontpage.html')

def signup(request):
    if request.method=='POST':
        form=SignUpFrom(request.POST)
        if form.is_valid():
            user=form.save()
            login(request,user)
            return redirect('frontpage')
    form=SignUpFrom()
    return render(request,"chatapp/signup.html",{'form':form})

