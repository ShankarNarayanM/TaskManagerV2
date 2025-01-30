from django import forms 
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from .models import Contact
from myapp.models import PriorityModel, StatusModel, TaskBoard

class Contact(forms.ModelForm):
    username = forms.CharField(label="username",max_length=100,required=True)
    email = forms.EmailField(label="email", max_length=100,required=True)
    message = forms.CharField(label="message",required=True)

    class Meta:
        model = Contact
        fields = ['username','email','message']

class Register(forms.ModelForm):
    username = forms.CharField(label="username", max_length=100,required=True)
    email = forms.EmailField(label="email", max_length=100,required=True)
    password = forms.CharField(label="password", max_length=100,required=True)
    confirm_password = forms.CharField(label="confirm_password", max_length=100,required=True)

    class Meta:
        model = User
        fields = ['username','email','password']

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')

        if password and confirm_password and password!=confirm_password:
            raise forms.ValidationError("Password mismatch")

class LoginForm(forms.Form):
    username = forms.CharField(label="username", max_length=100,required=True)
    password = forms.CharField(label="password", max_length=100,required=True)
    
    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get('username')
        password = cleaned_data.get('password')

        if username and password:
            user = authenticate(username=username, password=password)
            if user is None:
                raise forms.ValidationError("Invalid username and password")

class ForgotPasswordForm(forms.Form):
    email = forms.EmailField(label="email", max_length=100,required=True)

    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get('email')    

        if not User.objects.filter(email=email).exists():
            raise forms.ValidationError("No user found.")
        
class ResetPasswordForm(forms.Form):
    new_password = forms.CharField(label='new_password',min_length=8)
    confirm_new_password = forms.CharField(label='confirm_new_password',min_length=8)

    def clean(self):
        cleaned_data = super().clean()
        new_password = cleaned_data.get('new_password')
        confirm_new_password = cleaned_data.get('confirm_new_password')

        if new_password and confirm_new_password and new_password!=confirm_new_password:
            raise forms.ValidationError("Password mismatch")
        
class TaskForm(forms.ModelForm):
    taskname = forms.CharField(label="taskname", max_length=100,required=True)
    description = forms.CharField(label="description",max_length=250,required=False)
    start_date = forms.DateField(label="start_date",required=False)
    end_date = forms.DateField(label="end_date",required=False)
    status = forms.ModelChoiceField(label="status",queryset=StatusModel.objects.all(),required=False)
    priority = forms.ModelChoiceField(label="priority",queryset=PriorityModel.objects.all(),required=False)
    progress = forms.IntegerField(label="progress",max_value=100,required=False)
    user_id = forms.ModelChoiceField(label="user_id",queryset=User.objects.all(),required=True)
    class Meta:
        model = TaskBoard
        fields = ['taskname','description','start_date','end_date','status','priority','progress','user_id']

    def clean(self):
        cleaned_data = super().clean()
        taskname = cleaned_data.get('taskname') 

        if taskname and len(taskname) < 5:
            raise forms.ValidationError("Task name should have minimum 5 characters")