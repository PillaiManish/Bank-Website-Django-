from django.shortcuts import render,redirect
from django.contrib.auth.models import User, auth
from .models import customer_complaints
# Create your views here.


def f_complaints(request):
    if request.user.is_authenticated():  # is user is logined then continue
            
        if request.method == 'POST':
            userid = request.user.id
            subject = request.POST['subject']
            complaint = request.POST['complaint']

            user_complaints = customer_complaints(userid=userid,subject=subject,complaint=complaint)
            user_complaints.save()
            return redirect('/admins/login')

            # error conditions
        else:
            return render(request,'complaint_register.html',)
    else:
        return redirect('/')

def f_all_complaints(request): 
    if request.user.is_authenticated():  # is user is logined then continue
        self_userid = request.user.id
        all_complaints = customer_complaints.objects.filter(userid=self_userid)
        return render(request,'complaints_detail.html',{'user_complaint':all_complaints})
    
    else:
        return redirect('/admins/login')
