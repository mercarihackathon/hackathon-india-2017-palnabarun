from datetime import datetime
import json

import web

from .db import Sensor as db_sensor, Agent as db_agent
from .helpers import jsonapi, handle_new_data

s = db_sensor()
a = db_agent()

urls = (
	'/agents', 					'AgentAll',
	'/agent/([a-zA-Z0-9])', 	'Agent',
	'/sensors', 				'SensorAll',
	'/sensor/([a-zA-Z0-9])', 	'Sensor',
	'/data',					'Data'
	'/job',						'Job'
	)

def notfound():
	msg = json.dumps({"message": "not found"})
	headers = {"Content-Type": "application/json"}
	return web.HTTPError("404 Not Found", headers, msg)


class AgentAll:
	@jsonapi
	def GET(self):
		return a.list()

	def POST(self):
		data = json.loads(web.data().decode('utf-8'))
		return a.add(**data)

class SensorAll:
	@jsonapi
	def GET(self):
		return s.list()

	def POST(self):
		data = json.loads(web.data().decode('utf-8'))
		return a.add(**data)

class Sensor:
	@jsonapi
	def PUT(self, label):
		data = json.loads(web.data().decode('utf-8'))
		id = a.modify(id=label, **data)
		handle_new_data(label, data, s, a)

class Agent:
	pass

class Job:
	pass

if __name__ == '__main__' :
	app = web.application(urls, globals())
	app.notfound = notfound
	app.run()