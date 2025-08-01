from django.shortcuts import redirect, render
from django.contrib import messages
from django.views.decorators.http import require_POST
from django.contrib.auth.models import User
from django.contrib import auth

def login(request):

    if request.user.is_authenticated:
        return redirect('index')

    if request.method == 'POST':
        u_name = request.POST.get('u_name')
        c_pass = request.POST.get('c_pass')
        
        user = auth.authenticate(username=u_name,password=c_pass)

        if user is not None:
            auth.login(request,user)

            if user.is_superuser:
                return redirect('/admin/')
            else:
                return redirect('todo/index')
        else:
            messages.error(request,"Invalid MailId or Password")
            return render(request,'login.html')
    else:
        return render(request,'login.html')

def signup(request):

    if request.user.is_authenticated:
        return redirect('index')

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
        
        if status=="user":
            user = User.objects.create_user(username=u_name,first_name=f_name,last_name=l_name,email=email,password=pass1,is_active=True,is_staff=False,is_superuser=False)
            user.save()
        elif status=="staff":
            user = User.objects.create_user(username=u_name,first_name=f_name,last_name=l_name,email=email,password=pass1,is_active=True,is_staff=True,is_superuser=False)
            user.save()
        elif status=="admin":
            user = User.objects.create_user(username=u_name,first_name=f_name,last_name=l_name,email=email,password=pass1,is_active=True,is_staff=False,is_superuser=True)
            user.save()
        else:
            messages.error(request,'Error While SignUp')
            return render(request,'signup.html')
        
        return render(request,'login.html')
    else:
        return render(request,'signup.html')
    
@require_POST
def signout(request):
    user = request.user
    if user.is_authenticated:
        auth.logout(request)
    return redirect('/')
