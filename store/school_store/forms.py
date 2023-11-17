from django import forms
from .models import Course,Department,Purpose

class RegistrationForm(forms.Form):
    # Your existing form fields

    department = forms.ModelChoiceField(queryset=Department.objects.all())
    courses = forms.ModelChoiceField(queryset=Course.objects.none())
    purpose = forms.ModelChoiceField(queryset=Purpose.objects.all())