from django.forms import (
    ModelForm, Select, DateInput
)
from .models import User


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = [
            'email', 'first_name', 'last_name',
            'dob', 'address', 'phone', 'country',
            'state', 'city', 'position', 'gender',
            'marital_status', 'work_status', 'date_employed',
            'work_type', 'bio', 'department', 'avatar'
        ]
        widgets = {
            'position': Select(attrs={'class': 'form-control'}),
            'marital_status': Select(attrs={'class': 'form-control'}),
            'work_status': Select(attrs={'class': 'form-control'}),
            'gender': Select(attrs={'class': 'form-control'}),
            'work_type': Select(attrs={'class': 'form-control'}),
            'department': Select(attrs={'class': 'form-control'}),
            'date_employed': DateInput(attrs={'class': 'form-control', 'placeholder': 'yyyy-mm-dd'}),
            'dob': DateInput(attrs={'class': 'form-control', 'placeholder': 'yyyy-mm-dd'})
        }
