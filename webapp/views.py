from django.shortcuts import render, HttpResponseRedirect
from webapp import views
from .forms import AccountForm
from .models import Account
# Create your views here.
def add(request):
    if request.method=='POST':
        fm=AccountForm(request.POST)
        if fm.is_valid():
            ei=fm.cleaned_data['email_id']
            ai = fm.cleaned_data['account_id']
            an = fm.cleaned_data['account_name']
            reg=Account(email_id=ei,account_id=ai,account_name=an)
            reg.save()
            fm = AccountForm()
    else:
        fm=AccountForm()
    stud=Account.objects.all()
    return render(request,'enroll/addandshow.html ',{'form':fm,'stu':stud})

def delete(request,id):
    if request.method=='POST':
        pi=Account.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/add')

def update(request,id):
    if request.method=='POST':
        pi=Account.objects.get(pk=id)
        fm=AccountForm(request.POST, instance=pi)
        if fm.is_valid():
            fm.save()
    else:
        pi = Account.objects.get(pk=id)
        fm = AccountForm(instance=pi)
    return render(request,'enroll/update.html',{'form':fm})

