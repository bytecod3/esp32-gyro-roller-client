from tkinter import *

class App():
	def __init__(self, parent):
		self.parent = parent
		
		self.create_widgets()
		
		self.label_config = {
			"font": ("Arial", 12, "normal"),
            "pady": 5
		}
		
		
	def create_widgets(self):
		self.mainframe = Frame(self.parent)
		self.mainframe.grid(row=0, column=0)
		
		self.apptitle = Label(self.mainframe, text="GYRO GLOVE ANIMATOR")
		self.apptitle.grid(row=0, column=0)
		
		self.checkboxframe = Frame(self.mainframe)
		self.checkboxframe.grid(row=1, column=0)
		
		self.oncheckbox = Checkbutton(self.checkboxframe, text="On")
		self.oncheckbox.grid(row=0, column=0)
		
		self.oncheckbox = Checkbutton(self.checkboxframe, text="Off")
		self.oncheckbox.grid(row=0, column=1)
		
		self.oncheckbox = Checkbutton(self.checkboxframe, text="LOCK")
		self.oncheckbox.grid(row=0, column=2)
		
		# create canvas
		self.canvas = Canvas(self.mainframe, bg="black", width=700, height=650)
		self.canvas.grid(row=2, column=0, rowspan=4)
		
		self.animate()
	
	def animate(self):
		self.canvas.create_line(200, 200, 130, 150, fill="green")

		
	

	
def run_app():
	root = Tk()
	root.geometry("700x700")
	root.title("Gyro Glove Client")
	root.resizable(False, False)
	main = App(root)
	root.mainloop()		
		
		
if __name__ == "__main__":
	run_app()
	
