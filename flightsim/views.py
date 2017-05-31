from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import ensure_csrf_cookie
from django.views import generic

from datetime import datetime
from datetime import timezone
import json
import math
import random
import re

from . models import Plane, Flight
from . stats import calculateCorrelation

def arrivals(request):
	latest_arrivals_list = Flight.objects.exclude(arrival_time__isnull=True).order_by('-arrival_time')[:5];
	context = {'latest_arrivals_list': latest_arrivals_list};
	return render(request, 'arrivals.html', context);

def departures(request):
	latest_departures_list = Flight.objects.exclude(departure_time__isnull=True).order_by('-departure_time')[:5];
	context = {'latest_departures_list': latest_departures_list};
	return render(request, 'departures.html', context);

def stats(request):
	sql_waitingTime =("SELECT id, "
		"(JULIANDAY(arrival_time) - JULIANDAY(departure_time)) * 24 * 60 * 60 AS interval "
		"FROM flightsim_Flight "
		"WHERE arrival_time IS NOT NULL");
	
	waitingTimes = [];
	for f in Flight.objects.raw(sql_waitingTime):
		waitingTimes.append(f.interval);
	
	sql_maxWaitingTime =("SELECT id, "
		"(MAX(JULIANDAY(arrival_time)-JULIANDAY(departure_time))) * 24 * 60 * 60 AS maxTime "
		"FROM flightsim_Flight "
		"WHERE arrival_time IS NOT NULL");
		
	for f in Flight.objects.raw(sql_maxWaitingTime):
		maxWaitingTime = f.maxTime;
		
	sql_minWaitingTime =("SELECT id, "
		"(MIN(JULIANDAY(arrival_time)-JULIANDAY(departure_time))) * 24 * 60 * 60 AS minTime "
		"FROM flightsim_Flight "
		"WHERE arrival_time IS NOT NULL");
		
	for f in Flight.objects.raw(sql_minWaitingTime):
		minWaitingTime = f.minTime;
	
	sql_departureTime =("SELECT id, "
		"(JULIANDAY(departure_time) - "
		"(SELECT AVG(JULIANDAY(departure_time)) FROM flightsim_Flight WHERE arrival_time IS NOT NULL)"
		") * 24 * 60 * 60 AS dTime "
		"FROM flightsim_Flight "
		"WHERE arrival_time IS NOT NULL");
	
	departureTimes = [];
	for f in Flight.objects.raw(sql_departureTime):
		departureTimes.append(f.dTime);
		
	sql_arrivalTime =("SELECT id, "
		"(JULIANDAY(arrival_time) - "
		"(SELECT AVG(JULIANDAY(arrival_time)) FROM flightsim_Flight WHERE arrival_time IS NOT NULL)"
		") * 24 * 60 * 60 AS aTime "
		"FROM flightsim_Flight "
		"WHERE arrival_time IS NOT NULL");
	
	arrivalTimes = [];
	for f in Flight.objects.raw(sql_arrivalTime):
		arrivalTimes.append(f.aTime);
	
	context = {'waitingTimes':waitingTimes,
				'maxWaitingTime':maxWaitingTime,
				'minWaitingTime':minWaitingTime,
				'times':zip(departureTimes,arrivalTimes),
				'r':calculateCorrelation(departureTimes,arrivalTimes),
				};
	return render(request, 'stats.html', context);

@ensure_csrf_cookie
def index(request):
	return render(request,'index.html');
	
def generateFlight():
	planes = Plane.objects.all();
	plane_count = planes.count();
	plane_no = random.randint(0,plane_count-1);
		
	flight = Flight(flight_no=getFlightNo(), departure_time=datetime.now(timezone.utc), plane=planes[plane_no]);
	flight.save();
	return flight;

def getFlightNo():
	#Generate flight_no
	flight_no = "";
	for i in range(0,2):
		flight_no += getLetter();
	for i in range(0,3):
		flight_no += getDigit();
	return flight_no;
	
def getLetter():
	return chr(random.randint(ord('A'),ord('Z')));

def getDigit():
	return str(random.randint(0,9));
	
def getTimeArray(flight):
	#2017-04-11 20:29:11.190276+0:00
	regularExpression = "(\d{4})-(\d{2})-(\d{2})\s+(\d{2}):(\d{2}):(\d+\.*\d*).*";
	
	match = re.match(regularExpression, str(flight.departure_time));
	return match.groups();
	
def generate(request):
	flight = generateFlight();
		
	data = {
		'flight_id': flight.id,
		'flight_no': encrypt(flight.flight_no),
		'departure_time': getTimeArray(flight),
		'plane': {
			'name':flight.plane.name,
			'type':flight.plane.type,
		},
	}
	return JsonResponse(data);

"""Encrypt the string and return the ciphertext"""
def encrypt(plaintext):
	key = 14;

	dictionary = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789';
	
	result = "";
	
	for l in plaintext:
		i = (dictionary.index(l) + key) % 36;
		result += dictionary[i];
		
	return result;


def land(request):
	id = request.POST['flight_id'];

	try:
		flight = Flight.objects.get(id=id);
	except ObjectDoesNotExist:
		return JsonResponse({'successful' : False});
	else:
		flight.gate_no = request.POST['gate_no'];
		flight.arrival_time = datetime.now(timezone.utc);
	
	try:
		a=1;
		flight.save();
	except Exception:
		return JsonResponse({'successful' : False});
	else:
		return JsonResponse({'successful' : True, 'arrival_time':json.dumps(flight.arrival_time.isoformat())});