from django.contrib.auth import forms
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from django import forms as django_forms

from .models import User


class UserChangeForm(forms.UserChangeForm):
    class Meta(forms.UserChangeForm.Meta):
        model = User


class UserCreationForm(forms.UserCreationForm):
    email = django_forms.EmailField(required=True,
                                    label='Email',
                                    error_messages={'exists': 'Oops'})

    class Meta(forms.UserCreationForm.Meta):
        model = User
        fields = ("username", "email", "password1", "password2")

    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user

    def clean_email(self):
        if User.objects.filter(email=self.cleaned_data['email']).exists():
            raise ValidationError(
                self.fields['email'].error_messages['exists'])
        return self.cleaned_data['email']
