# dappx/views.py
from django.shortcuts import render
from dappx.forms import UserForm, UserProfileInfoForm
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
import json
import conekta

conekta.api_key = "key_znUnfNpt8zDvdnJY9rYZHQ"
conekta.api_version = "2.4.0"
conekta.locale = 'es'

def index(request):
    return render(request,'dappx/index.html')
@login_required
def special(request):
    return HttpResponse("You are logged in !")
@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

def register(request):
    registered = False
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            if 'profile_pic' in request.FILES:
                print('found it')
                profile.profile_pic = request.FILES['profile_pic']
            profile.save()
            registered = True
        else:
            print(user_form.errors,profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()
    return render(request,'dappx/registration.html',
                          {'user_form':user_form,
                           'profile_form':profile_form,
                           'registered':registered})

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse("Your account was inactive.")
        else:
            print("Someone tried to login and failed.")
            print("They used username: {} and password: {}".format(username,password))
            return HttpResponse("Invalid login details given")
    else:
        return render(request, 'dappx/login.html', {})
    
    
def my_user_login2(request):
    if request.method == 'POST':
        print(request.POST.get('token'));
    else:
        return render(request, 'dappx/login.html', {})
    
    
def my_user_login(request):
    registered = False
    if request.method == 'POST':
        registered = False
        token = dict(request.POST.lists())["token[id]"][0]
        name = dict(request.POST.lists())["name"][0]
        email = dict(request.POST.lists())["email"][0]
        phone = dict(request.POST.lists())["phone"][0]
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.token = token
            profile.name = name
            profile.email = email
            profile.phone = phone
            if 'profile_pic' in request.FILES:
                print('found it')
                profile.profile_pic = request.FILES['profile_pic']
            #Create customers
            try:
                customer = conekta.Customer.create({
                'name': name,
                'email': email,
                'phone': phone,
                'payment_sources': [{
                  'type': 'card',
                  'token_id': token
                }]
              })
            except conekta.ConektaError as e:
              print (e)
            
            subscription = customer.createSubscription({
              "plan": "LaPapa"
            })
            profile.pay = True;
            user.save()
            profile.save()
            registered = True
        else:
            print(user_form.errors,profile_form.errors)
    else:
        return render(request, 'dappx/login.html', {})
    return render(request,'dappx/registration.html',
                          {'user_form':user_form,
                           'profile_form':profile_form,
                           'registered':registered})
    

import smtplib
def webhook(request):
    #data = json.loads(request.body)
    #if data.type == 'charge.paid':
      #payment_method = data.charges.data.object.payment_method.type
      #payment_method = "asd"
      #msg['Subject'] = 'Pago ' + payment_method + ' confirmado'
      #msg['From'] = me
      #msg['To'] = you
    
      server = smtplib.SMTP('smtp.gmail.com', 25)
      server.connect('smtp.gmail.com', 465)
      server.login("erichris2902@gmail.com", "Annieteamo1");
      msg = "Header\nBody!" # The /n separates the message from the headers
      server.sendmail("erichris2902@gmail.com", "erichris@live.com.mx", msg.as_string())
      server.quit()
      return render(request, 'dappx/login.html', {})
        
    
