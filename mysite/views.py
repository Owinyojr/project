from django.shortcuts import render,HttpResponse,redirect
from django.core.mail import EmailMultiAlternatives
from django.conf import settings
from django.contrib import messages
from django.template.loader import render_to_string
from .models import Book
from .forms import RegistrationForm
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required(login_url='signin')
def index(request):
    if request.method=='POST':
        name=request.POST['name']
        email=request.POST['email']
        subj=request.POST['subject']
        msg=request.POST['message']
        subject='People Enquiries'
        context={
            'name':name,
            'email':email,
            'message':msg
        }
        html_message = render_to_string('email_template.html', context)
        try:
            email = EmailMultiAlternatives(
                subject, 
                msg, 
                email,  
                [settings.EMAIL_HOST_USER],  
                reply_to=[email], 
            )
            email.attach_alternative(html_message, "text/html")
            email.send()
            messages.success(request,f'Dear , {name} we have received your message and we will get back to you shortly')
        except Exception as e:
            print(e)
            messages.warning(request,'Please check your internet and try again')
    return render(request,'index.html')



def register(request):
    form=RegistrationForm
    if request.method=='POST':
        form=RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data.get('username')
            messages.success(request,f"Account created for {username}")
            return redirect('signin')
    context={
        "forms":form
    }
    return render(request,'register.html',context)


def signin(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            messages.success(request,f"Welcome {username} to TracoAgency")
            return redirect('index')
        else:
            messages.warning(request,'You have entered wrong credentials')
            return redirect('signin')
    return render(request,'login.html')



def trackbook(request):
    if request.method=='POST':
        name=request.POST['name']
        email=request.POST['email']
        phone=request.POST['phone']
        date=request.POST['date']
        time=request.POST['time']
        farmsize=request.POST['people']
        message=request.POST['message']
        print(name,phone)
        Book.objects.create(
            name=name  ,
            email=email,
            phone=phone,
            date=date,
            time=time,
            farmsize=farmsize,
            message=message
        )
        messages.success(request,'Your booking has been recieved , we will get back to you')
    return redirect('index')
        


def signout(request):
    logout(request)
    messages.warning(request,'You have been logged out')
    return redirect('signin')




def adminpage(request):
    data=Book.objects.all()
    context={
        'datas':data
    }
    return render(request,'admin.html',context)
