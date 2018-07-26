from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.core.checks import messages
from django.template.context_processors import request
from django.views import View
from django.views.generic import DetailView,ListView,CreateView,UpdateView,DeleteView
from onlineapp.views import *
from onlineapp.models import *
from django.shortcuts import render, get_object_or_404
from django import forms
from django.urls import reverse_lazy
from django.shortcuts import *

class SignUpForm(forms.Form):
    first_name = forms.CharField(label='FirstName',widget=forms.TextInput)
    last_name =  forms.CharField(label='LastName',widget=forms.TextInput)
    username =  forms.CharField(label='UserName',widget=forms.TextInput)
    password =  forms.CharField(label='PassWord',widget=forms.TextInput)

class CreateUserView(View):

    template_name = 'auth_form.html'
    form_class = SignUpForm

    def get(self,request):
        pass
        signup_form = SignUpForm()
        return render(request,template_name = 'auth_form.html',context={'signup_form':signup_form})

    def post(self, request, *args, **kwargs):
        pass
        form = SignUpForm(request.POST)
        #import ipdb
        #ipdb.set_trace()
        if form.is_valid():
            user = User.objects.create_user(**form.cleaned_data)
            user.save()
            user = authenticate(request,username=form.cleaned_data['username'],password=form.cleaned_data['password'])
            if user is not None:
                #login(request,user)
                return redirect('/colleges/')
            else:
                messages.error(request,"Invalid Credentials")

class LoginForm(forms.Form):
    pass
    username = forms.CharField(label='UserName', widget=forms.TextInput)
    password = forms.CharField(label='PassWord', widget=forms.TextInput)

class LoginView(View):
    pass
    template_name = 'login_form.html'
    form_class = LoginForm

    def get(self, request):
        pass
        login_form = LoginForm()
        return render(request, template_name='login_form.html', context={'login_form': login_form})

    def post(self, request):
        pass
        form = LoginForm(request.POST)
        # import ipdb
        # ipdb.set_trace()
        username = request.POST['username']
        password = request.POST['password']
        if form.is_valid():
            #user = User.objects.create_user(**form.cleaned_data)
            #user.save()
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request,user)
                return redirect('/colleges/')
            else:
                messages.error(request, "Invalid Credentials")

def LogoutView(request):
    logout(request)
    return redirect('/login/')

