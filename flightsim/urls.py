from django.conf.urls import url

from . import views

app_name = 'flightsim'
urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^generate$',views.generate,name='generate'),
	url(r'^land$',views.land,name='land'),
	url(r'^arrivals$',views.arrivals,name='arrivals'),
	url(r'^departures$',views.departures,name='departures'),
	url(r'^stats$',views.stats,name='stats'),
	]