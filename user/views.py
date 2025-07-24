from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib import messages

from django.contrib.auth.models import User
from django.contrib import auth

def login(request):

    if request.method == 'POST':
        u_name = request.POST.get('u_name')
        c_pass = request.POST.get('c_pass')
        
        user = auth.authenticate(username=u_name,password=c_pass)
        print(user)
        if user is not None:
            auth.login(request,user)
            redirect('todo/')
        else:
            messages.error(request,"Invalid MailId or Password")
            return render(request,'login.html')
    else:
        return render(request,'login.html')

def signup(request):

    if request.method == 'POST':
        u_name = request.POST.get('u_name')
        f_name = request.POST.get('f_name')
        l_name = request.POST.get('l_name')
        email = request.POST.get('email')
        pass1 = request.POST.get('pass')
        c_pass = request.POST.get('c_pass')
        status = request.POST.get('status')
        
        if pass1!=c_pass:
            messages.error(request,'Password Not Matched')
            return render(request,'signup.html')
        
        # user = User.objects.create_user(username=u_name,first_name=f_name,last_name=l_name,email=email,password=pass1,is_active=true)
        # user.save()
        
        return render(request,'login.html')
    else:
        return render(request,'signup.html')