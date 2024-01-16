from django.contrib import admin
from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from .models import Service

class ServiceAdminForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = '__all__'

class ServiceAdmin(admin.ModelAdmin):
    form = ServiceAdminForm

admin.site.register(Service, ServiceAdmin)
