from tkinter import *
from math import *
from time import sleep
import http.client
from random import randint
from datetime import datetime


root = Tk()

HOST = "192.168.207.36"
PORT = 80


connection = http.client.HTTPConnection(HOST, PORT, timeout=10)

y_offset = 350
x_offset = 200

label_config = {
	"font": ("Arial", 12, "normal"),
	"pady": 5
}

mainframe = Frame(root)
mainframe.grid(row=0, column=0)

apptitle = Label(mainframe, text="GYRO GLOVE ANIMATOR")
apptitle.grid(row=0, column=0)

checkboxframe = Frame(mainframe)
checkboxframe.grid(row=1, column=0)

oncheckbox = Checkbutton(checkboxframe, text="ON")
oncheckbox.grid(row=0, column=0)

oncheckbox = Checkbutton(checkboxframe, text="OFF")
oncheckbox.grid(row=0, column=1)

oncheckbox = Checkbutton(checkboxframe, text="LOCK")
oncheckbox.grid(row=0, column=2)

# restart button
restartbutton = Button(checkboxframe, text="RESTART", bg="orange", font=("bold", 18), relief=RAISED)
restartbutton.grid(row=0, column=3)

# create canvas
canvas = Canvas(mainframe, bg="black", width=700, height=650)
canvas.grid(row=2, column=0, rowspan=4)



# create line data list [x1, y1, x2, y2]
line_data = [700-x_offset, y_offset, x_offset, y_offset]

# calculate the line length
line_length = sqrt( pow((line_data[2] - line_data[0]), 2) + pow( (line_data[-1] - line_data[1]), 2) )

print(f"line length: {line_length}")

# calculate the line radius
line_radius = line_length / 2
	

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
	
	canvas.create_rectangle(0,0, 700, 700, fill="black")
	
	# roller parameters
	canvas.create_text(500, 10, text="Latency :", fill="yellow")
	canvas.create_text(550, 10, text=randint(600, 650), fill="yellow")
	
	canvas.create_text(500, 25, text="Roll angle: ", fill="yellow")
	canvas.create_text(550, 25, text=theta, fill="yellow")
	
	canvas.create_text(500, 40, text="Timestamp: ", fill="yellow")
	canvas.create_text(600, 40, text=now.time(), fill="yellow")
	
	

	canvas.create_line(x_coordinate_inverse+x_offset, y_coordinate_inverse+y_offset, x_coordinate+x_offset, y_coordinate+y_offset, width=10, fill="green")
	
	root.update()
			
			
root.geometry("700x700")
root.title("Gyro Glove Client")
root.resizable(False, False)
main = App(root)
root.mainloop()		
		
		
	
