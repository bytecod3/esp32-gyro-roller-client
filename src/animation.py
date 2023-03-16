from tkinter import *
from math import *
from time import sleep
import http.client
from random import randint
from datetime import datetime


root = Tk()
root.title("Gyro Glove Client")

HOST = "192.168.168.36"
PORT = 80

connection = http.client.HTTPConnection(HOST, PORT, timeout=10)

now = datetime.now()

y_offset = 300
x_offset = 500

label_config = {
	"font": ("Arial", 13, "normal"),
	"pady": 5
}

mainframe = Frame(root)
mainframe.grid(row=0, column=0)

# apptitle = Label(mainframe, text="GYRO GLOVE ANIMATOR")
# apptitle.grid(row=0, column=0)

dframe = Frame(mainframe)
dframe.grid(row=0, column=0)
canvasframe = Frame(mainframe)
canvasframe.grid(row=0, column=1)

checkboxframe = LabelFrame(dframe, text="Controls", font=("bold", 18), padx=15)
checkboxframe.grid(row=0, column=0)

oncheckbox = Checkbutton(checkboxframe, text="ON")
oncheckbox.grid(row=0, column=0)

oncheckbox = Checkbutton(checkboxframe, text="OFF")
oncheckbox.grid(row=1, column=0)

oncheckbox = Checkbutton(checkboxframe, text="LOCK")
oncheckbox.grid(row=2, column=0)

# log data button
logdatabutton = Button(checkboxframe, text="Log data", bg="gray", font=("bold", 18), relief=RAISED, padx=20)
logdatabutton.grid(row=3, column=0)

# restart button
restartbutton = Button(checkboxframe, text="Restart  ", bg="orange", font=("bold", 18), relief=RAISED, padx=20)
restartbutton.grid(row=4, column=0)

# create canvas
canvas = Canvas(canvasframe, bg="black", width=900, height=700)
canvas.grid(row=0, column=0)

# create line data list [x1, y1, x2, y2]
line_data = [700-x_offset, y_offset, x_offset, y_offset]

# calculate the line length
line_length = sqrt( pow((line_data[2] - line_data[0]), 2) + pow( (line_data[-1] - line_data[1]), 2))

# calculate the line radius
line_radius = line_length / 2

# DATA
# data frame
dataframe = LabelFrame(dframe, text="Position",  font=("bold", 18), padx=25)
dataframe.grid(row=1, column=0)

rolllabel = Label(dataframe, label_config, text="Roll angle: ")
rolllabel.grid(row=1, column=0)

roll = Label(dataframe,label_config, text="0")
roll.grid(row=1, column=1)

pitchlabel = Label(dataframe, label_config, text="Pitch angle: ")
pitchlabel.grid(row=2, column=0)

pitch = Label(dataframe, label_config, text="0")
pitch.grid(row=2, column=1)

yawlabel = Label(dataframe, label_config, text="Yaw angle: ")
yawlabel.grid(row=3, column=0)

yaw = Label(dataframe, label_config, text="0")
yaw.grid(row=3, column=1)


dataframetiming = LabelFrame(dframe, text="Timing",  font=("bold", 18), padx=25)
dataframetiming.grid(row=2, column=0)
latencylabel = Label(dataframetiming, label_config, text="Latency: ")
latencylabel.grid(row=1, column=0)

latency = Label(dataframetiming, label_config, text=randint(50, 70))
latency.grid(row=1, column=1)

timelabel = Label(dataframetiming, label_config, text="Time: ")
timelabel.grid(row=2, column=0)

time = Label(dataframetiming, label_config, text=now.strftime("%H:%M:%S"))
time.grid(row=2, column=1)


dataframenetwork = LabelFrame(dframe, text="Network",  font=("bold", 18), padx=25)
dataframenetwork.grid(row=3, column=0)
serverIPlabel = Label(dataframenetwork, label_config, text="Server: ")
serverIPlabel.grid(row=1, column=0)

server = Label(dataframenetwork, label_config, text=HOST)
server.grid(row=1, column=1)

clientlabel = Label(dataframenetwork, label_config, text="Clients[3]: ")
clientlabel.grid(row=2, column=0)

client = Label(dataframenetwork, label_config, text="MG 996R")
client.grid(row=2, column=1)


exitframe = Frame(dframe)
exitframe.grid(row=4, column=0)

exitbutton = Button(exitframe, text="EXIT",  fg="red", font=("Arial", 18))
exitbutton.grid(row=0, column=0)

while True:
	connection.request("GET", "/get_roll")
	response = connection.getresponse()
	
	theta = int(float(response.read().decode("utf-8")))
	
	now = datetime.now()				

	# calculate the polar coordinates given theta
	x_coordinate = cos(radians(theta)) * line_radius
	y_coordinate = -sin(radians(theta)) * line_radius
	
	# get the inverses of these coordinates
	x_coordinate_inverse = -cos(radians(theta)) * line_radius
	y_coordinate_inverse = sin(radians(theta)) * line_radius
	
	canvas.create_rectangle(0,0, 1000, 700, fill="black")
	canvas.create_text(130, 55, text=theta, fill="yellow", font=("Roboto", 13))

	canvas.create_line(x_coordinate_inverse + x_offset, y_coordinate_inverse + y_offset, x_coordinate + x_offset, y_coordinate + y_offset, width=10, fill="green")

	roll.config(text=theta)
	latency.config(text=randint(50, 60))
	time.config(text=now.strftime("%H:%M:%S"))

	root.update()

root.mainloop()		
		
		
	
