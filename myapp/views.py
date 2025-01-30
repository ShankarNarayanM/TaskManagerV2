from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponse
from .forms import TaskForm, ForgotPasswordForm, LoginForm, Register, Contact, ResetPasswordForm
from .models import PriorityModel, StatusModel, TaskBoard
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
import logging
from django.contrib.auth.models import User
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.core.mail import send_mail
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.
def landingPage(request):
    return render(request,'landingPage.html')

def loginPage(request):
    form = LoginForm()
    username = request.POST.get('username')
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username,password=password)
            if user is not None:
                auth_login(request,user)
                return redirect("/dashboard")
        else:
            return render(request,"login.html",{'form':form,'username':username})

    return render(request,"login.html",{'form':form})

def registerPage(request):
    logger = logging.getLogger("TESTING")
    username = request.POST.get('username')
    email = request.POST.get('email')

    if request.method == "POST":
        form = Register(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            return redirect("/login")
        else:
            logger.debug("Failure")
        return render(request, "register.html",{"form":form,"username":username,"email":email})
    return render(request, "register.html")

def TaskList(request):
    tasks = TaskBoard.objects.filter(user_id=request.user.id)

    return render(request,'Taskboard.html',{'tasks': tasks})

def contacts(request):
    if request.method == 'POST':
        form = Contact(request.POST)
        username = request.POST.get('username')
        email = request.POST.get('email')
        message = request.POST.get('message')
        logger = logging.getLogger("TESTING")
        
        if form.is_valid():
            logger.debug(form.cleaned_data['username'])
            success_message = "Your response is recorded"
            form.save()
            return render(request,'contact.html',{'form':form,'success_message':success_message})
        else:
            logger.debug("Failure")
            logger.debug(message)
            return render(request,'contact.html',{'form':form, 'username':username, 'email':email, 'message':message})
    return render(request,'contact.html')

def dashboard(request):
    return render(request,'dashboardPage.html')

def logout(request):
    auth_logout(request)
    return redirect("landingPage")

def pricing(request):
    return render(request,'pricingPage.html')

def forgotPassword(request):
    form = ForgotPasswordForm()
    if request.method == 'POST':
        form = ForgotPasswordForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            user = User.objects.get(email=email)
            token = default_token_generator.make_token(user)
            uid = urlsafe_base64_encode(force_bytes(user.pk))
            current_site = get_current_site(request)
            domain = current_site.domain
            subject = "Reset Password Requested"
            message = render_to_string("reset_password_email.html",{
                'username':user.username,
                'domain':domain,
                'uid':uid,
                'token':token
            })
            send_mail(subject,message,'noreply@example.com',[email])
            messages.success(request,"Email sent successfully")
    return render(request,'forgotPasswordPage.html',{'form':form})

def resetPassword(request, uidb64, token):
    form = ResetPasswordForm()
    if request.method == 'POST':
        form = ResetPasswordForm(request.POST)
        if form.is_valid():
            new_password = form.cleaned_data['new_password']
            uid = urlsafe_base64_decode(uidb64)
            try:
                user = User.objects.get(pk=uid)
            except:
                user = None 
            if user is not None and default_token_generator.check_token(user, token):
                user.set_password(new_password)
                user.save()
                messages.success(request, 'Your password has been updated successfully')
                return redirect('loginPage')
            else: 
                messages.error(request, 'Reset password link is expired')
    return render(request, 'resetPasswordPage.html',{'form':form})

@login_required
def addTask(request):
    statuses = StatusModel.objects.all()
    priorities = PriorityModel.objects.all()

    form = TaskForm()
    if request.method == 'POST':
        form = TaskForm(request.POST)  
        if form.is_valid():
            post = form.save()
            return redirect('taskListPage')
        else:
            print("Errors")
    return render(request, 'addTask.html',{'statuses':statuses,'priorities':priorities,'form':form})

@login_required
def editTask(request, task_id):
    statuses = StatusModel.objects.all()
    priorities = PriorityModel.objects.all()
    task = get_object_or_404(TaskBoard, id=task_id)
    form = TaskForm()
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            messages.success(request,"Your task has been updated")
            return redirect('taskListPage')
    return render(request, 'editTask.html',{'statuses':statuses,'priorities':priorities,'task':task,'form':form})

@login_required
def deleteTask(request, task_id):
    task = get_object_or_404(TaskBoard, id=task_id)
    task.delete()
    messages.success(request,"Your task has been deleted")
    return redirect('taskListPage')

@login_required
def myProfile(request):
    return render(request, "myProfile.html")


