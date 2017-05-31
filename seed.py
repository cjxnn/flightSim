import django
django.setup();

from flightsim.models import Plane

with open("input.csv") as file:
	data = file.readlines();
	for line in data:
		words = line.strip().split(",");
		name = words[0].upper();
		type = words[1].upper();
		Plane(name=name, type=type).save();