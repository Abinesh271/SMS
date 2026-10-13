from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Student


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ["full_name", "email", "mobile", "course", "age"]
        widgets = {
            "full_name": forms.TextInput(attrs={"placeholder": "Enter your Name"}),
            "email": forms.EmailInput(attrs={"placeholder": "Enter your @gmail.com"}),
            "mobile": forms.TextInput(attrs={"placeholder": "+91 8928404890"}),
            "course": forms.Select(),
            "age": forms.NumberInput(attrs={"placeholder": "23", "min": 15, "max": 100}),
        }

    def clean_age(self):
        age = self.cleaned_data["age"]
        if not 15 <= age <= 100:
            raise forms.ValidationError("Age must be between 15 and 100.")
        return age


class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={"placeholder": "Enter your gmail.com"}))
    first_name = forms.CharField(max_length=50, required=True, widget=forms.TextInput(attrs={"placeholder": "First name"}))
    last_name = forms.CharField(max_length=50, required=False, widget=forms.TextInput(attrs={"placeholder": "Last name"}))

    class Meta:
        model = User
        fields = ("username", "first_name", "last_name", "email", "password1", "password2")
