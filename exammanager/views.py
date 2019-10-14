from django.shortcuts import render, redirect
from exammanager.models import *
from django.forms import ModelForm
from django.contrib import messages
from django import forms

#classes for forms
class LoginForm(ModelForm):
    class Meta:
        model = AddStudent
        fields = ['roll','password']

class RegisterForm(forms.ModelForm):
    s = [("1", "1 semester"), ("2", "2 semester"), ("3", "3 semester"), ("4", "4 semester"), ("5", "5 semester"), ("6", "6 semester"), ("7", "7 semester"), ("8", "8 semester") ]
    d = [("Computer Science", "Computer Science"), ("Electronics", "Electronics"), ("Mechanical", "Mechanical"), ("Civil", "Civil"), ("5", "IT"), ("Electrical", "Electrical"), ("Production", "Production") ]
    roll = forms.CharField(max_length=20, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': "Enter Roll No."}))
    name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': "Enter Name"}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': "Enter Email"}))
    password = forms.CharField(max_length=10, widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': "Enter Password"}))
    department = forms.ChoiceField(label="Department :", choices=d)
    semester = forms.ChoiceField(label="Semester :", choices=s)
    dob = forms.DateField()
    class Meta:
        model = AddStudent
        fields = ['roll','name', 'email', 'password', 'department', 'semester', 'dob']






# Create your views here.
def viewhall(request, template_name="exammanager/viewhall.html"):
    login_status = request.session['login_status']
    roll = request.session['roll']
    try:
        s = Allocate.objects.get(roll=roll)
    except:
        s = "Null"
    if(login_status=="1"):
        data = {"login_status":login_status, 's':s ,'roll':roll}
        return render(request, template_name, data)
    else:
        return redirect('home')


def dashboard(request, template_name="exammanager/dashboard.html"):
    login_status = request.session['login_status']
    email = request.session['email']
    s = AddStudent.objects.get(email=email)
    if(login_status=="1"):
        data = {"login_status":login_status, 's':s }
        return render(request, template_name, data)
    else:
        return redirect('home')


def logout(request):
    # clear the session here...
    request.session['login_status'] = None
    return redirect('home')


def home(request, template_name="exammanager/home.html"):

    return render(request, template_name)


def login(request, template_name="exammanager/login.html"):
    request.session['login_status'] = "0"
    form = LoginForm(request.POST)
    if (form.is_valid()):
        roll = request.POST['roll']
        password = request.POST['password']
        try:
            b = AddStudent.objects.get(roll=roll, password=password)
        except:
            b = False
            messages.error(request, "Please Enter Valid Roll No. & Password")
        if (b):
            # set the session here...
            request.session['login_status'] = "1"
            request.session['name'] = b.name
            request.session['email'] = b.email
            request.session['roll'] = b.roll
            return redirect('dashboard')
        else:
            return redirect('login')
    return render(request, template_name)


def admin(request):
    return redirect('http://localhost:8000/admin/')





def register(request, template_name="exammanager/register.html"):
    form = RegisterForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('login')
    return render(request, template_name, {"form": form})







