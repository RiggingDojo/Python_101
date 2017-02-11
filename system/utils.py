import pymel.core as pm 
import json
import tempfile

def writeJson(fileName, data):
	with open(fileName, 'w') as outfile:
		json.dump(data, outfile)
	file.close(outfile)

def readJson(fileName):
	with open(fileName, 'r') as infile:
		data = (open(infile.name, 'r').read())
	return data