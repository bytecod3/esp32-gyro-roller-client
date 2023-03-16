# this program gets the data from HTTP server(glove)
import http.client

# esp32 glove host and port
HOST = "192.168.8.36"
PORT = 80

connection = http.client.HTTPConnection(HOST, PORT, timeout=10)

while True:
	connection.request("GET", "/get_roll")
	response = connection.getresponse()
	print(f"Response: {response.read()}")


