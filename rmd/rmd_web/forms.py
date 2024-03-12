from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User, Review, Post, Comment, Person
import json

# -----------------------------------
# Authentication Forms
# -----------------------------------

# Form for registering a new user with email as username, including password confirmation.
class SignUpForm(UserCreationForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['email','password1', 'password2']
        # fields = ['email','name', 'password1', 'password2']
        
    #  Ensure that the two password entries match.
    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords do not match")
        return password2

# Form for logging in a user using their email and password.
class UserLoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)

class UserProfileForm(forms.Form):
    email = forms.EmailField(label='Email', required=True)
    full_name = forms.CharField(label='Full Name', max_length=255, required=True)
    profile_picture = forms.URLField(label='Profile Picture URL', required=False)
    professional_background = forms.CharField(label='Professional Background', widget=forms.Textarea, required=False)
    
    # Interests are handled separately as checkboxes in the template, so they're not explicitly defined here
    
    privacy_settings = forms.CharField(label='Privacy Settings', widget=forms.Textarea, required=False,
                                       help_text='Enter privacy settings in JSON format.')

    def clean_privacy_settings(self):
        privacy = self.cleaned_data.get('privacy_settings')
        try:
            privacy_json = json.loads(privacy)
        except json.JSONDecodeError:
            raise forms.ValidationError('Invalid JSON format for privacy settings.')
        return privacy_json

    def clean(self):
        cleaned_data = super().clean()
        # Perform any additional custom validation here
        return cleaned_data

# -----------------------------------
# Core Application Forms
# -----------------------------------

# Form for creating a new post related to a person, capturing the content and how the user met the person.
class PostForm(forms.ModelForm):
    class Meta:
        model = Post  # Specifies the model to use
        fields = ['content', 'how_met']  # Specifies the fields to include in the form


# Form for adding a new person profile, including first and last name, Instagram handle, and join date.
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

# Form for adding a review about a person, including the content of the review and how they met.
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
        