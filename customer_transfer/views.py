from django.shortcuts import render,redirect
from .models import customer_transfer
from admin_account.models import account_balance
# Create your views here.
def f_customer_transfer(request):
    if request.user. is_authenticated():
            
        if request.method == 'POST':
            
            self_user = request.user.username
            self_userid = request.user.id
            to_userid = request.POST['to_userid']      
            to_amount = request.POST['to_amount']
            



            # update from account balance
            account_balances = account_balance.objects.get(userid=self_userid)

            if int(account_balances.balance) < int(to_amount):
                return render(request,'c_transfer.html',{'msg':'Unsuccessful : Low Balance in account'})            
            
            # update to account balance
            try:
                account_balances_to = account_balance.objects.get(userid=to_userid)
            except:
                return render(request,'c_transfer.html',{'msg':'Unsuccessful : No such beneficiary'})
            
            account_balances.balance = int(account_balances.balance) - int(to_amount)
            account_balances.save()

            account_balances_to.balance = int(account_balances_to.balance) + int(to_amount)
            account_balances_to.save()


            user_transfer = customer_transfer(self_userid=self_userid,to_userid=to_userid,to_amount=to_amount)
            user_transfer.save()

            return redirect('/customer/transfer/')
        return render(request,'c_transfer.html',)
    
    else:
        return redirect('/admins/login')


def f_customer_transaction(request):
    if request.user. is_authenticated():
        self_userid = request.user.id
        all_transaction_to = customer_transfer.objects.filter(self_userid=self_userid)

        all_transaction_from = customer_transfer.objects.filter(to_userid=self_userid)

        account_balances = account_balance.objects.filter(userid=self_userid)

        return render(request,'transaction_detail(user).html',{'user_trans':all_transaction_to,'from_users':all_transaction_from,'balances':account_balances})

    else:
        return redirect('/admins/login')