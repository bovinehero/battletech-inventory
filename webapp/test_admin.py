from django.test import TestCase
from django.contrib.admin.sites import AdminSite
from .models import Pilot, Mech
from .admin import PilotAdmin, MechAdmin


class MockRequest(object):
    pass

request = MockRequest()


class TestAdmin(TestCase):

    def setUp(self):
        self.pilot_admin = PilotAdmin(Pilot, AdminSite())
        self.mech_admin = MechAdmin(Pilot, AdminSite())

    def test_approve_pilot_approves(self):
        pilot = Pilot.objects.create(
            callsign='Test Pilot',
            status=0
            )
        queryset = Pilot.objects.filter(callsign='Test Pilot')
        self.pilot_admin.approve_pilot(request, queryset)
        self.assertEqual(Pilot.objects.get(callsign='Test Pilot').status, 1)

    def test_revoke_pilot_revokes(self):
        pilot = Pilot.objects.create(
            callsign='Test Pilot',
            status=1
            )
        queryset = Pilot.objects.filter(callsign='Test Pilot')
        self.pilot_admin.revoke_pilot(request, queryset)
        self.assertEqual(Pilot.objects.get(callsign='Test Pilot').status, 0)

    def test_approve_mech_approves(self):
        mech = Mech.objects.create(
            name='Test Mech',
            status=0
            )
        queryset = Mech.objects.filter(name='Test Mech')
        self.mech_admin.approve_mech(request, queryset)
        self.assertEqual(Mech.objects.get(name='Test Mech').status, 1)

    def test_revoke_mech_revokes(self):
        mech = Mech.objects.create(
            name='Test Mech',
            status=1
            )
        queryset = Mech.objects.filter(name='Test Mech')
        self.mech_admin.revoke_mech(request, queryset)
        self.assertEqual(Mech.objects.get(name='Test Mech').status, 0)