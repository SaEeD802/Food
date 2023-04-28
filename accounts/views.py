from django.shortcuts import render
from .forms import RegisterForm
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect


# Create your views here.
# عملیات ثبت نام رو انجام بدیم
# نام کاربری و ایمیل نباید تکراری باشه
# چک بشه اطلاعات از اپ یوزر
# پسوردها باید مثل هم باشن
# ارور بده زمانی که نکات بالا رعایت نشد
# اگر اطلاعات دریافتی مشکلی نداشت ثبت نام انجام شود

def user_register(request):
    template='registration/signup.html'
    if request.method == 'POST':
        form=RegisterForm(request.POST)
        if form.is_valid():
           if User.objects.filter(username=form.cleaned_data['username']).exists():
               return render(request,template,{
                   'form':form,
                   'error_message':'Username already exitsts.'  
               })
           elif  User.objects.filter(email=form.cleaned_data['email']).exists():
               return render(request,template,{
                   'form':form,
                   'error_message':'email already exitsts.'  
               })
           elif form.cleaned_data['password']!=form.cleaned_data['password_repeat']:
                return render(request,template,{
                   'form':form,
                   'error_message':'passwords to not match.'  
               })
           else:
               user=User.objects.create_user(
                   form.cleaned_data['username'],
                   form.cleaned_data['email'],
                   form.cleaned_data['password']
               )     
               user.save()
               return HttpResponseRedirect('login')
           
    else:
        form=RegisterForm()
    
    return render(request,template,{'form':form}) 