from django import forms
from .models import Jedi, Candidate, Tests, Questions

class CandidateForm(forms.ModelForm):
    class Meta:
        model = Candidate
        fields = [
            'name',
            'planet',
            'age',
            'email',
        ]

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'planet': forms.Select(attrs={'class': 'form-control'}),
            'age': forms.NumberInput(attrs={'class': 'form-control'})
        }

class CandidateTest(forms.ModelForm):
    class Meta:
        model = Questions
        fields = [
            'text',
        ]

        widgets = {
        }