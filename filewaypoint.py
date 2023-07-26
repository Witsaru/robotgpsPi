import numpy as np

def read_mp():
	rawlist = []
	waylist = []
	with open("Waypoint.waypoints", 'r') as file:
		for line in file:
			d_data = line.replace('\t', ' ')
			rawlist.append(d_data)
			
		rawlist = rawlist[1::]
		
		for i in rawlist:
			n = list(i.split(" "))
			lat = float(n[8])
			lon = float(n[9])
			path = (lat,lon)
			waylist.append(path)
			
		return waylist
