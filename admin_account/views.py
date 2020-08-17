from django.shortcuts import render,redirect
from django.contrib.auth.models import User, auth
from .models import account_balance
# Create your views here.
def f_admin_login(request):
    if request.user. is_authenticated():  # is user is logined then continue
        return redirect('/')
    
    else:
        if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']

            user = auth.authenticate(username=username,password=password)

            if user is not None:
                auth.login(request,user)
                return redirect('/admins/login')

            # error conditions
            else:
                return redirect('/admins/login')
        else:
            return render(request,'login.html',)

def f_logout(request):
    if request.user. is_authenticated():  # is user is logined then continue
        auth.logout(request)
        return redirect('/')
    else:
        return redirect('/admins/login')


def f_user_registration(request):
    if request.user. is_authenticated():
        # if only admin then continue   
        return redirect('/')


    else:
        if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']
            first_name = request.POST['first_name']
            last_name = request.POST['last_name']
            email = request.POST['email']

            
            try:
                username_already_taken = User.objects.filter(username_exact=username)
                return render(request,'registration.html',{'msg':'Username is already taken'})

            
            
            
            except:
                new_user = User.objects.create_user(username=username,password=password,first_name=first_name,last_name=last_name,email=email)
                new_user.save()


                user_id_registered = User.objects.get(username=username)


                # user id or user name check it
                default_balance = account_balance(userid = user_id_registered.id)
                default_balance.balance=1000
                default_balance.save()
                return redirect('/')    
                
        return render(request,'registration.html',)





def f_forgot_password(request):
    if request.user.is_authenticated():
        return redirect('/')
    else:
        if request.method == 'POST':
            username = request.POST['username']
            id = request.POST['id']
            email = request.POST['email']
            password = request.POST['password']

            try:
                user = User.objects.get(username=username,email=email,id=id)
                user.set_password(password)
                user.save()

                return redirect('/admins/login')

            except:
                return redirect('/forgot') # it must be render

    return render(request,'forgot_password.html',)


def f_set_new_password(request):
    pass