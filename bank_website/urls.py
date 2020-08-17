"""bank_website URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from admin_account.views import f_admin_login,f_logout,f_user_registration,f_forgot_password
from customer_transfer.views import f_customer_transfer,f_customer_transaction
from complaint.views import f_complaints,f_all_complaints
from homepage.views import f_homepage,f_accountdetail
from django.contrib.auth.views import password_change

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^admins/login/', f_admin_login),
    url(r'^logout/', f_logout),
    url(r'^register/', f_user_registration), 
    url(r'^customer/transfer/', f_customer_transfer),
    url(r'^customer/transaction_details', f_customer_transaction),
    url(r'^customer/complaints', f_complaints),
    url(r'^customer/complaintdetails', f_all_complaints),
    url(r'^accountinfo', f_accountdetail),
    url(r'^forgot/', f_forgot_password),
    # url(r'^password-change/',password_change , name='password_change'),
    url(r'^$', f_homepage),




    
]
