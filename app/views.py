from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
# Create your views here.
from django.contrib.auth import login,authenticate,logout
from app.forms import *
from django.urls import reverse

from django.contrib.auth.decorators import login_required
from decimal import Decimal

def base(request):
    return render(request, 'base.html')



def home(request):
    if request.session.get('username'):
        username=request.session.get('username')
        d={'username':username}
        return render(request,'home.html',d)
    return render(request,'home.html')


def user_login(request):
    if request.method=='POST':
        username=request.POST['un']
        password=request.POST['pw']
        user=authenticate(username=username,password=password)

        if user and user.is_active:
            login(request,user)
            request.session['username']=username
            return HttpResponseRedirect(reverse('home'))
        else:
            return HttpResponse('u r not an authenticated user')
    return render(request,'user_login.html')

def wallet(request):
    return render(request, 'wallet.html')

@login_required
def send_money(request):
    if request.method=='POST':
        reuser=request.POST['reuser']
        amount=float(request.POST['amount'])
        sender=request.session.get('username')
        so=User.objects.get(username=sender)
        ro=User.objects.get(username=reuser)
        wso=Wallet.objects.get(user=so)
        wro=Wallet.objects.get(user=ro)
        if so.user_type=='PREMIUM':
            samount=decimal.Decimal(amount*1.03)
        else:
            samount=decimal.Decimal(amount*1.05)
        
        if ro.user_type=='PREMIUM':
            ramount=decimal.Decimal(amount*.99)
        else:
            ramount=decimal.Decimal(amount*.97)
        print(samount,type(samount))
        print(wso.balance,type(wso.balance))
        if wso.balance>=samount:
            wso.balance-=samount
            wro.balance+=ramount
            return HttpResponse('Amount sent successfully')
        else:
            return HttpResponse('Insufficient Balance')



        




    return render(request, 'send_money.html')

def Request_money(request):
    return render(request, 'Request_money.html')

def Received_Request(request):
    return render(request, 'Received_Request.html')


def registration(request):
    FO=UserForm()
    d={'form':FO}
    if request.method=='POST':
        fd=UserForm(request.POST)
        if fd.is_valid():
            uso=fd.save(commit=False)
            pw=fd.cleaned_data.get('password')
            uso.set_password(pw)
            uso.save()
            return HttpResponse('Registration is done')

    return render(request,'registration.html',d)


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('home'))





