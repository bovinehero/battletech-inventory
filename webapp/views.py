from django.shortcuts import HttpResponse, render, get_object_or_404, reverse
from django.views import generic, View
from django.http import HttpResponseRedirect
from django.contrib import messages
from .models import Pilot, Mech

class PilotList(generic.ListView):
    model = Pilot
    queryset = Pilot.objects.filter(status=1).order_by('callsign')
    template_name = 'pilots.html'
    paginate_by = 6

class MechList(generic.ListView):
    model = Mech
    queryset = Mech.objects.filter(status=1).order_by('name')
    template_name = 'index.html'
    paginate_by = 6