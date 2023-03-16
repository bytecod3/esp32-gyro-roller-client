# this program gets the data from HTTP server(glove)
import http.client
import RPi.GPIO as GPIO
from time import sleep

# esp32 glove host and port
HOST = "192.168.207.36"
PORT = 80

# create servo object
servopin = 18
GPIO.setmode(GPIO.BCM)
GPIO.setup(servopin, GPIO.OUT)

p = GPIO.PWM(servopin, 50) # use 50Hz
p.start(2.5)

connection = http.client.HTTPConnection(HOST, PORT, timeout=10)

try:
	while True:
		connection.request("GET", "/get_roll")
		response = connection.getresponse()
	
		roll_angle = int(float(response.read().decode("utf-8")))
		
		#convert angle to pwm
		pwm = (roll_angle)/10 + 2.5
	
		# process this value to get the absolute value
		p.ChangeDutyCycle(pwm)
		sleep(0.2)

except KeyboardInterrupt:
	p.stop()
	GPIO.cleanup()


