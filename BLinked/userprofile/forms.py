from django import forms
from django_countries.fields import CountryField
from blink.models import User
from django.forms import ModelForm


class AddEducationForm(forms.Form):
    schoolName = forms.CharField(label='School Name', max_length=100)
    degree = forms.CharField(label='Degree', max_length=100)
    fieldOfStudy = forms.CharField(label='Field of study', max_length=100)
    startYear = forms.IntegerField(label='Start Year', required=False)
    endYear = forms.IntegerField(label='End Year', required=False)
    additionalNotes = forms.CharField(label='Additional Notes', widget=forms.Textarea, max_length=1024, required=False)
    json = forms.FileField(label='Upload JSON Certificate')


GENDER_CHOICES = (
    ('M', 'Male'),
    ('F', 'Female'),
)


class EditDetailsForm(ModelForm):
    class Meta:
        model = User
        exclude = ['username', 'password']

    name = forms.CharField(label='Full Name', max_length=100)
    country = CountryField().formfield(label='Country')
    gender = forms.ChoiceField(label='Gender', choices=GENDER_CHOICES)
    dateOfBirth = forms.DateField(label='Date of Birth', required=False, help_text="yyyy-mm-dd")
    profilePhoto = forms.ImageField(label='Profile Photo', required=False)
    mobileNumber = forms.CharField(label='Mobile Number', max_length=20, required=False)
    address = forms.CharField(label='Address', required=False)
    summary = forms.CharField(label='Professional summary', widget=forms.Textarea, required=False)
