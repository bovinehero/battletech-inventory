from django import forms
from .models import Mech

class CreateMechForm(forms.ModelForm):
    
    class Meta:
        model = Mech
        fields = [
            'name',
            'category',
            'weight',
            'tech_level',
            'role',
            'slug',
            'stock',
            'description',
            'record_sheet',
            'battle_value',
            'status'
        ]
        