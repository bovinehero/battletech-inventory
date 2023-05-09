from django.test import TestCase
from .models import Pilot, Mech, TECH, ROLE, CLASSIFICATION, WEIGHTS, STATUS

# TODO write all test cases for the models.

class TestModels(TestCase):

    def test_pilot_defaults(self):
        pilot = Pilot.objects.create(
            callsign='Test Pilot'
            )
        self.assertEqual(pilot.status, 0)
        self.assertEqual(pilot.gunnery, 4)
        self.assertEqual(pilot.piloting, 5)
        self.assertEqual(pilot.experience, 1000)
        self.assertEqual(pilot.edge, 1)

    def test_mech_defaults(self):
        pilot = Pilot.objects.create(
            callsign='Test Pilot'
            )
        mech = Mech.objects.create(
            name='Test Mech',
            pilot=pilot
            )
        self.assertEqual(mech.status, 0)
        self.assertEqual(mech.category, 0)
        self.assertEqual(mech.weight, 0)
        self.assertEqual(mech.tech_level, 0)
        self.assertEqual(mech.role, 0)
        self.assertEqual(mech.stock, 2)
        self.assertEqual(mech.description, '')
        self.assertEqual(mech.record_sheet, '')
        self.assertEqual(mech.battle_value, 9999)
        self.assertEqual(mech.status, 0)

    def test_mech_string_method_returns_callsign(self):
        pilot = Pilot.objects.create(
            callsign='Test Pilot'
            )
        self.assertEqual(str(pilot), 'Test Pilot')

    def test_mech_string_method_returns_name(self):
        pilot = Pilot.objects.create(
            callsign='Test Pilot'
            )
        mech = Mech.objects.create(
            name='Test Mech',
            pilot=pilot
            )
        self.assertEqual(str(mech), 'Test Mech')
        
