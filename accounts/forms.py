from django import forms

# username
# email
# pass1
# pass2

class RegisterForm(forms.Form):
    username=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    email=forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}))
    password=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password_repeat=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))