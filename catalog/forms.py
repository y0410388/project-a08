from django import forms


class UserForm(forms.Form):
    username = forms.CharField(label="User Name", max_length=128)
    password = forms.CharField(label="Password", max_length=256, widget=forms.PasswordInput)

class RegisterForm(forms.Form):
    gender = (
        ('male',"Male"),
        ('female',"Female"),
    )
    username = forms.CharField(label="User Name", max_length=128, widget=forms.TextInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(label="Password", max_length=256, widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label="ConFirm Password", max_length=256, widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(label="Email Address", widget=forms.EmailInput(attrs={'class': 'form-control'}))
    sex = forms.ChoiceField(label='Sex', choices=gender)