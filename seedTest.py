import django
django.setup();

from flightsim.models import Plane

# Test if the fleet has 9 planes
assert (Plane.objects.count() == 9),"Fleet has other than 9 planes!";

# Test if the fleet has A380
assert (len(Plane.objects.filter(name="A380")) == 1),"Fleet does not have A380!";

# Test if the fleet has B777
assert (len(Plane.objects.filter(name="B777")) == 1),"Fleet does not have B777!";

# Test if the fleet has three plane types
assert (len(set(map(lambda p: p.type, Plane.objects.all()))) == 3),"Fleet has other than 3 plane types!";

# Test if the fleet has plane types S,M,L
assert (len(Plane.objects.filter(type="S")) > 0),"Fleet does not have plane type S!";
assert (len(Plane.objects.filter(type="M")) > 0),"Fleet does not have plane type M!";
assert (len(Plane.objects.filter(type="L")) > 0),"Fleet does not have plane type L!";