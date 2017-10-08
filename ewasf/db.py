import os
import web

db = web.database(web.config.get('EWAS_DB_URI'))

class Sensor:
	def __init__(self):
		self.db = db

	def add(self, label, lat, lon, threshold):
		self.db.insert('sensors', label=label, lat=lat, lon=lon, threshold=threshold, flag=False)

	def modify(self, label, **kwargs):
		self.db.update('sensors', where='label=$label', vars={'label': label}, **kwargs)

	def add_entry(self, label, flow):
		sensor = self.list(label=label)
		self.db.insert('sensor_data', sensor_id=sensor.id, flow=flow)

	def list(self, **kwargs):
		return self.db.where('sensors', order='id desc', **kwargs).list()


class Agent:
	def __init__(self):
		self.db = db

	def add(self, name):
		self.db.insert('agents', name=name)

	def modify(self, name, **kwargs):
		self.db.update('agents', where='name=$name', vars={'name': name}, **kwargs)

	def list(self, **kwargs):
		return self.db.where('agents', order='id desc', **kwargs).list()

