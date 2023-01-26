from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User
from django.core.exceptions import ValidationError


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=30, required=True)
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')
    address = forms.CharField(max_length=50)
    phone_number = forms.CharField(max_length=50)
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'password1', 'password2', 'image')


    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        print(self.cleaned_data)
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        user.first_name = self.cleaned_data['first_name']
        user.last_name  = self.cleaned_data['last_name']
        user.username = self.cleaned_data['email'].split('@')[0]
        user.set_password(self.cleaned_data['password2'])
        user.image = self.cleaned_data['image']

        if commit:
            user.save()
        return user