from django.shortcuts import HttpResponse, render, get_object_or_404, reverse
from django.contrib.messages import get_messages
from django.test import TestCase
from . import views
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
        bv_mod = views.PilotDetail.bv_modifier(self, queryset[0].gunnery,queryset[0].piloting)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(bv_mod, 1)

    def test_get_active_mech_detail(self):
        mech = Mech.objects.create(
            name='testm',
            slug='testm',
            status='1'
        )
        pilot = Pilot.objects.create(
            callsign='testp',
            slug='testp',
            status='1'
            )
        activeMech = ActiveMech.objects.create(
            name='test',
            pilot=pilot,
            mech=mech,
            slug='testor',
            status='1'
        )
        queryset = ActiveMech.objects.filter(name=activeMech.name)
        self.assertEqual(queryset[0].name, activeMech.name)
        response = self.client.get(f'/{queryset[0].slug}')
        self.assertEqual(response.status_code, 200)

    def test_toggle_mech_status(self):
        mech = Mech.objects.create(
            name='testm',
            slug='testm',
            status='1'
        )
        response = self.client.get(f'/mechs/{mech.slug}/toggle/')
        self.assertRedirects(response, '/mechs/')
        updated_mech = Mech.objects.get(name=mech.name)
        self.assertEquals(updated_mech.status, 0)
        response = self.client.get(f'/mechs/{updated_mech.slug}/toggle/')
        updated_mech_again = Mech.objects.get(name=mech.name)
        self.assertEquals(updated_mech_again.status, 1)

    def test_create_mech_form_is_valid(self):
        data = {
            'name' : 'testm',
            'category' : 0,
            'weight' : 0,
            'slug' :'testm',
            'status' : 0,
            'tech_level' : 0,
            'role' : 0,
            'description' : 'Test description',
            'record_sheet' : 'custom',
            'battle_value' : 9999

        }
        form = views.CreateMechForm(data=data)
        print(form)
        self.assertTrue(form.is_valid())
        # response = self.client.post('/mechs/create/', data=data)
        # print(response.context)
        # messages = list(response.context['messages'])
        # self.assertEqual(len(messages), 1)
        # self.assertEqual(str(messages[0]), 'my message')
        # messages = list(get_messages(form.wsgi_request))
        
