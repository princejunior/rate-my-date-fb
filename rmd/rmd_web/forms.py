# forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.forms.widgets import PasswordInput
from .models import User, Review, Post, Comment, Person  # Importing models

# Creates a form for adding a post for the date
class PostForm(forms.ModelForm):
    class Meta:
        model = Post  # Specifies the model to use
        fields = ['content', 'how_met']  # Specifies the fields to include in the form

# Creates a form for adding a profile for the date 
class PersonForm(forms.ModelForm):
    class Meta:
        model = Person  # Specifies the model to use
        fields = ['first_name', 'last_name', 'instagram', 'joined_date']  # Specifies the fields to include in the form
        widgets = {
            'joined_date': forms.DateInput(attrs={'type': 'date'}),  # Specifies the widget for the joined_date field
        }
        required = {
            'joined_date': False,  # Makes joined_date field optional
        }

class ReviewForm(forms.ModelForm):
    content = forms.CharField(
        label='Your Review',
        widget=forms.Textarea(attrs={'rows': 3}),
        required=False
    )

    how_met = forms.CharField(
        label='How did you meet?',
        max_length=100
    )

    class Meta:
        model = Review
        fields = ['content', 'how_met']  # Exclude time_created field


# AUTHENTICATION
class SignUpForm(UserCreationForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['email','password1', 'password2']
        # fields = ['email','name', 'password1', 'password2']

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords do not match")
        return password2

class UserLoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)