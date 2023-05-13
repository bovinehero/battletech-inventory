from django.shortcuts import HttpResponse, render, get_object_or_404, reverse
from django.test import TestCase
from .views import PilotList, PilotDetail, MechList, MechDetail, ActiveMech, ActiveMechList
from .models import Pilot, Mech, ActiveMech


class TestViews(TestCase):

    def test_get_active_mech_list(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')

    def test_get_mech_list(self):
        response = self.client.get('/mechs/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'mechs.html')

    def test_get_pilot_list(self):
        response = self.client.get('/pilots/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'pilots.html')

    def test_get_mech_detail(self):
        pass
        mech = Mech.objects.create(
            name='testor',
            slug='testor',
            status='1'
        )
        queryset = Mech.objects.filter(name=mech.name)
        self.assertEqual(queryset[0].name, mech.name)
        response = self.client.get(f'/mechs/{queryset[0].slug}')
        self.assertEqual(response.status_code, 200)

    def test_get_pilot_detail(self):
        pilot = Pilot.objects.create(
            callsign='testor',
            slug='testor',
            status='1'
            )
        queryset = Pilot.objects.filter(callsign=pilot.callsign)
        self.assertEqual(queryset[0].callsign, pilot.callsign)
        response = self.client.get(f'/pilots/{queryset[0].slug}')
        bv_mod = PilotDetail.bv_modifier(self, queryset[0].gunnery,queryset[0].piloting)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(bv_mod, 1)