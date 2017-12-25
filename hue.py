import time
from phue import Bridge

import pprint
pp=pprint.pprint

b = Bridge("192.168.178.32")

#pp(b.get_group())

def cycle_spots():
	lights = b.get_light_objects('id')
	while True:
		for l in [22, 18, 19, 21, 23, 24, 20]:
			lights[l].on = True
			time.sleep(.5)
			lights[l].on = False
	
def list_lights():
	lights = b.get_light_objects('list')
	for i, light in enumerate(lights):
		print i+1, light.name, light.on

def list_groups():
	for i in range(0, len(b.get_group())):
		print "Group: ", b.get_group(i, 'name') #, b.get_group(i, 'state')
		print "\tLights:", b.get_group(i, 'lights')

def all_lights_off():
	lights = b.get_light_objects('list')
	for i, light in enumerate(lights):
		light.on = False
		print i+1, light.name, light.on

def list_sensors():
	sensors = b.get_sensor_objects('list')
	for i, sensor in enumerate(sensors):
		if sensor.type == 'ZLLLightLevel':
			light = 'Dark' if sensor.state['dark'] else 'Day'
			print "%s - %s: Light %s %s" % (i, sensor.name, sensor.state['lightlevel'], sensor.state)
	for i, sensor in enumerate(sensors):
		if sensor.type == 'ZLLPresence':
			print "%s - %s Motion: %s" % (i, sensor.name, sensor.state['presence'])

#pp(b.get_api())		
#list_lights()
#list_groups()
list_sensors()
