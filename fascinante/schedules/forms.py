# SeuApp/forms.py
from django import forms
from .models import Scheduling
from services.models import Service

class SchedulingForm(forms.ModelForm):
    class Meta:
        model = Scheduling
        fields = '__all__'
    
    author = forms.CharField(max_length=200, label='Nome completo')
    checkin = forms.DateTimeField(label='Data e hora')