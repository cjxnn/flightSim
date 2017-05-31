from django.test import TestCase
from django.test.utils import setup_test_environment
from django.test import Client
from django.urls import reverse

from flightsim.models import Flight, Plane

import unittest

class DjangoTestCase(unittest.TestCase):
	def setUp(self):
		self.client = Client();
		self.loadFleet();
	
	def loadFleet(self):
		Plane(name = 'A380', type = 'L').save();
		Plane(name = 'A350', type = 'M').save();
		Plane(name = 'B747', type = 'L').save();
		Plane(name = 'B787', type = 'M').save();
		Plane(name = 'B777', type = 'S').save();
		Plane(name = 'A310', type = 'S').save();
		
	def test_flightsim(self):
		response = self.client.get('/flightsim');
		self.assertEqual(301, response.status_code);
	
	def test_index(self):
		response = self.client.get(reverse('flightsim:index'));
		self.assertEqual(200, response.status_code);
	
	def test_arrivals(self):
		response = self.client.get('/flightsim/arrivals');
		self.assertEqual(200, response.status_code);
	
	def test_departures(self):
		response = self.client.get('/flightsim/departures');
		self.assertEqual(200, response.status_code);
		
	def test_generate(self):
		response = self.client.get('/flightsim/generate',HTTP_X_REQUESTED_WITH='XMLHttpRequest');
		self.assertEqual(200, response.status_code);
		
	def test_land(self):
		response = self.client.get('/flightsim/generate',HTTP_X_REQUESTED_WITH='XMLHttpRequest');
		flight_id = response.json()['flight_id'];
		response = self.client.post('/flightsim/land',{'flight_id':flight_id, 'gate_no':1},HTTP_X_REQUESTED_WITH='XMLHttpRequest');
		self.assertEqual(200, response.status_code);
	
	def test_stats(self):
		response = self.client.get('/flightsim/generate',HTTP_X_REQUESTED_WITH='XMLHttpRequest');
		flight_id = response.json()['flight_id'];
		self.client.post('/flightsim/land',{'flight_id':flight_id, 'gate_no':1},HTTP_X_REQUESTED_WITH='XMLHttpRequest');
		
		response = self.client.get('/flightsim/generate',HTTP_X_REQUESTED_WITH='XMLHttpRequest');
		flight_id = response.json()['flight_id'];
		self.client.post('/flightsim/land',{'flight_id':flight_id, 'gate_no':1},HTTP_X_REQUESTED_WITH='XMLHttpRequest');
		
		response = self.client.get('/flightsim/stats');
		self.assertEqual(200, response.status_code);