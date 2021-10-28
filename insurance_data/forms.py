from django import forms
from .models import Insurance


class PolicyForm(forms.ModelForm):

    class Meta:
        model = Insurance
        fields = '__all__'

    
