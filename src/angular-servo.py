# this program gets the data from HTTP server(glove)
import http.client
from gpiozero import AngularServo
from time import sleep

# esp32 glove host and port
HOST = "192.168.207.36"
PORT = 80

# create servo object
servo = AngularServo(18, min_pulse_width=0.0006, max_pulse_width=0.0023)

connection = http.client.HTTPConnection(HOST, PORT, timeout=10)

while True:
	connection.request("GET", "/get_roll")
	response = connection.getresponse()
	
	roll_angle = int(float(response.read().decode("utf-8")))
	print(roll_angle)
		
	# process this value to get the absolute value
	servo.angle = roll_angle	
	
	
