from django import forms
from .models import Mech, Pilot

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
            'description',
            'record_sheet',
            'battle_value',
            'status'
        ]

class UpdateMechForm(forms.ModelForm):
    
    class Meta:
        model = Mech
        fields = [
            'name',
            'category',
            'weight',
            'tech_level',
            'role',
            'slug',
            'description',
            'record_sheet',
            'battle_value',
            'status'
        ]

class CreatePilotForm(forms.ModelForm):
    
    class Meta:
        model = Pilot
        fields = [
            'callsign',
            'gunnery',
            'piloting',
            'experience',
            'edge',
            'slug',
            'status'
        ]

class UpdatePilotForm(forms.ModelForm):
    
    class Meta:
        model = Pilot
        fields = [
            'callsign',
            'gunnery',
            'piloting',
            'experience',
            'edge',
            'slug',
            'status'
        ]