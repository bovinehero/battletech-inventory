from django.shortcuts import HttpResponse, render, get_object_or_404, reverse
from django.urls import reverse_lazy
from django.views import generic, View
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.http import HttpResponseRedirect
from django.contrib import messages
from .models import Pilot, Mech, ActiveMech
from .forms import MechForm
import numpy

class PilotList(generic.ListView):
    model = Pilot
    queryset = Pilot.objects.filter(status=1).order_by('callsign')
    template_name = 'pilots.html'
    paginate_by = 10

class MechList(generic.ListView):
    model = Mech
    queryset = Mech.objects.filter(status=1).order_by('pk')
    template_name = 'mechs.html'
    paginate_by = 10

class ActiveMechList(generic.ListView):
    model = ActiveMech
    queryset = ActiveMech.objects.filter(status=1).order_by('name')
    template_name = 'index.html'
    paginate_by = 10

class MechDetail(generic.ListView):
    
    def get(self, request, slug, *args, **kwargs):
        queryset = Mech.objects.filter(status=1)
        mech = get_object_or_404(queryset, slug=slug)
        return render(
            request,
            "mech_detail.html",
            {
                "mech": mech
            },
        )

class PilotDetail(View):

    def bv_modifier(self, gun_skill, pilot_skill):
        pilot_modifiers = numpy.array([
            [2.80, 2.63, 2.45, 2.28, 2.01, 1.82, 1.75, 1.67, 1.59],
            [2.56, 2.40, 2.24, 2.08, 1.84, 1.60, 1.58, 1.51, 1.44],
            [2.24, 2.10, 1.96, 1.82, 1.61, 1.40, 1.33, 1.31, 1.25],
            [1.92, 1.80, 1.68, 1.56, 1.38, 1.20, 1.14, 1.08, 1.06],
            [1.60, 1.50, 1.40, 1.30, 1.15, 1.00, 0.95, 0.90, 0.85],
            [1.50, 1.35, 1.26, 1.17, 1.04, 0.90, 0.86, 0.81, 0.77],
            [1.43, 1.33, 1.19, 1.11, 0.98, 0.85, 0.81, 0.77, 0.72],
            [1.36, 1.26, 1.16, 1.04, 0.92, 0.80, 0.76, 0.72, 0.68],
            [1.28, 1.19, 1.10, 1.01, 0.86, 0.75, 0.71, 0.68, 0.64]
        ])
        return pilot_modifiers[gun_skill][pilot_skill]

    def get(self, request, slug, *args, **kwargs):
        queryset = Pilot.objects.filter(status=1)
        pilot = get_object_or_404(queryset, slug=slug)
        bv_mod = self.bv_modifier(pilot.gunnery, pilot.piloting)
        return render(
            request,
            "pilot_detail.html",
            {
                "pilot": pilot,
                "bv_mod": bv_mod
            },
        )

class ActiveMechDetail(generic.ListView):
    
    def get(self, request, slug, *args, **kwargs):
        queryset = ActiveMech.objects.filter(status=1)
        active_mech = get_object_or_404(queryset, slug=slug)
        bv_mod = PilotDetail.bv_modifier(self, active_mech.pilot.gunnery, active_mech.pilot.piloting)
        return render(
            request,
            "active_mech_detail.html",
            {
                "active_mech": active_mech,
                "bv_mod": bv_mod
            },
        )
    
class CreateMechView(CreateView):

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
    template_name = 'mechs_form.html'

class UpdateMechView(UpdateView):
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
    template_name = 'mechs_form.html'


class DeleteMechView(DeleteView):
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
    template_name = 'mechs_form.html'    
    success_url = reverse_lazy("mechs")