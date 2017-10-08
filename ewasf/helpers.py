import functools
import json

from geopy.distance import great_circle
import web

from .db import Agent, Sensor
from .messaging import send_message

s = Sensor()
d = Agent()

def jsonapi(f):
	"""Decorator to simplify JSON APIs.
	"""
	@functools.wraps(f)
	def g(*a, **kw):
		try:
			response = f(*a, **kw)
		except web.HTTPError:
			raise
		except Exception as e:
			raise
			web.ctx.status = "500 Internal Error"
			response = {"error_message": str(e)}

		web.header("Access-Control-Allow-Origin", "*")
		if isinstance(response, (list, dict)):
			web.header("Content-Type", "application/json")
			return json.dumps(response, indent=True)
		else:
			return response
	return g

def handle_new_data(label, data):
	sensor = s.list(label=label)
	if sensor.threshold < data['flow']:
		agent = find_agent(sensor.lat, sensor.lon)
		send_message(agent, sensor)

def find_agent(lat, lon):
	agents = a.list()
	nearest_neighbor = None
	n_dist = 15000
	for agent in agents:
		dist = great_circle((agent.lat, agent.lon), (lat, lon)).miles
		if dist <= n_dist:
			n_dist = dist
			nearest_neighbor = agent
	return nearest_neighbor
