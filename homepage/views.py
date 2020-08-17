from django.shortcuts import render,redirect
from django.contrib.auth.models import User, auth
from admin_account.models import account_balance

# Create your views here.
def f_homepage(request):
    return render(request,'homepage.html',)


def f_accountdetail(request):
    if request.user. is_authenticated():
        user = User.objects.filter(username = request.user.username)
        user_balance = account_balance.objects.filter(userid=request.user.id)
        return render(request,'myaccountdetail.html',{'info':user,'balance':user_balance})

    else:
        return redirect('/admins/login')