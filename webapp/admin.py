from django.contrib import admin
from .models import Pilot, Mech, ActiveMech

# Register your models here.

@admin.register(Pilot)
class PilotAdmin(admin.ModelAdmin):
    list_display = ('callsign', 'slug', 'experience', 'gunnery', 'piloting', 'status')
    search_fields = ['callsign', 'gunnery']
    list_filter = ('experience', )
    prepopulated_fields = {'slug': ('callsign',)}
    actions = ['approve_pilot', 'revoke_pilot']

    def approve_pilot(self, request, queryset):
        queryset.update(status=1)
    
    def revoke_pilot(self, request, queryset):
        queryset.update(status=0)

@admin.register(Mech)
class MechAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'category',
        'weight',
        'tech_level',
        'role',
        'stock',
        'record_sheet',
        'battle_value',
        'status'
        ) 
    search_fields = ['type', 'tech_level']
    list_filter = ('tech_level', )
    actions = ['approve_mech', 'revoke_mech']
    prepopulated_fields = {'slug': ('name',)}

    def approve_mech(self, request, queryset):
        queryset.update(status=True)
    
    def revoke_mech(self, request, queryset):
        queryset.update(status=False)

@admin.register(ActiveMech)
class ActiveMechAdmin(admin.ModelAdmin):
    list_display = ('name', 'pilot', 'mech')
    prepopulated_fields = {
        'slug': ('name',)
    }