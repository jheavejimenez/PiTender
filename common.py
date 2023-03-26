#!/usr/bin/env python3

import time
import datetime
import os
import json

def ReadStatus():
	# *****************************************
	# Read State Values from File
	# *****************************************
	try:
		with open("status.json", "r") as json_data_file:
			json_data_string = json_data_file.read()
			status = json.loads(json_data_string)
	except (IOError, OSError):
		# Issue with reading states JSON, so create one/write new one

		status = {
			'status': {"active": 0, "progress": 0},
			'control': {
				"start": 0,
				"pause": 0,
				"stop": 0,
				"clean": "",
				"drink_name": "",
			},
		}

		WriteStatus(status)

	return(status)

def WriteStatus(status):
	# *****************************************
	# Write State Values to File
	# *****************************************
	json_data_string = json.dumps(status)
	with open("status.json", 'w') as status_file:
	    status_file.write(json_data_string)

def ReadSettings():
	# *****************************************
	# Read Settings from File
	# *****************************************

	# Read all lines of settings.json into an list(array)
	try:
		with open("settings.json", "r") as json_data_file:
			json_data_string = json_data_file.read()
			settings = json.loads(json_data_string)
	except (IOError, OSError):
		# Issue with reading states JSON, so create one/write new one

		settings = {
			'inventory': {
				"pump_01": "rum",
				"pump_02": "vodka",
				"pump_03": "whiskey",
				"pump_04": "coke",
				"pump_05": "oj",
				"pump_06": "tequila",
				"pump_07": "marg_mix",
				"pump_08": "iced_tea",
			},
			'assignments': {
				"pump_01": 17,
				"pump_02": 27,
				"pump_03": 22,
				"pump_04": 23,
				"pump_05": 24,
				"pump_06": 25,
				"pump_07": 2,
				"pump_08": 3,
			},
			'flowrate': 85,
		}

		WriteSettings(settings)

	return(settings)

def WriteSettings(settings):
	# *****************************************
	# Write all settings to JSON file
	# *****************************************
	json_data_string = json.dumps(settings)
	with open("settings.json", 'w') as settings_file:
	    settings_file.write(json_data_string)

def ReadDrinkDB():
	# *****************************************
	# Read Settings from File
	# *****************************************

	# Read all lines of settings.json into an list(array)
	try:
		with open("drink_db.json", "r") as json_data_file:
			json_data_string = json_data_file.read()
			drink_db = json.loads(json_data_string)
	except (IOError, OSError):
		# Issue with reading states JSON, so create one/write new one

		drink_db = {'drinks': {"empty": "Empty"}, 'ingredients': {"empty": "Empty"}}

	return(drink_db)

def WriteDrinkDB(drink_db):
	# *****************************************
	# Write drink_db to JSON file
	# *****************************************
	json_data_string = json.dumps(drink_db)
	with open("drink_db.json", 'w') as drinkdb_file:
	    drinkdb_file.write(json_data_string)

def WriteLog(event):
	# *****************************************
	# Function: WriteLog
	# Input: str event
	# Description: Write event to event.log
	#  Event should be a string.
	# *****************************************
	now = str(datetime.datetime.now())
	now = now[:19]

	with open("./logs/events.log", "a") as logfile:
		logfile.write(f'{now} {event}' + '\n')
