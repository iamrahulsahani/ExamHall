from exammanager.models import *
from django.contrib.auth.models import User

















# class userform(forms.ModelForm):
#     rollno = forms.CharField(widget=forms.TextInput( attrs = {'class':'form-conrol', 'placeholder':'Enter Roll No.'}), max_length=50)
#     email = forms.EmailField(widget=forms.EmailInput( attrs = {'class':'form-conrol', 'placeholder':'Enter Email'}), max_length=100)
#     name = forms.CharField(widget=forms.TextInput( attrs = {'class':'form-conrol', 'placeholder':'Enter Name'}), max_length=50)
#     password = forms.CharField(widget=forms.PasswordInput( attrs = {'class':'form-conrol', 'placeholder':'Enter Password'}), max_length=50)
#     confirm_password = forms.CharField(widget=forms.PasswordInput( attrs = {'class':'form-conrol', 'placeholder':'Confirm Password'}), max_length=50)
#
#     class Meta():
#         model = user
#         fields = ['rollno', 'email', 'name', 'password']