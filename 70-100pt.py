##########################################
#                                        #
#             Draw a house!              #
#                                        #
##########################################

# Use create_line(), create_rectangle() and create_oval() to make a 
# drawing of a house using the tKinter Canvas widget.

# 70pt: House outline (roof and the house)
# 80pt: Square windows and a door
# 90pt: A door handle plus a chimney!
# 100pt: Green grass on the ground and a red house!

# Minus 5pts if your code has no comments
# Minus 10pts if you only commit once to github

from Tkinter import *
root = Tk()

# Create the canvas widget
drawpad = Canvas(root, width=800,height=600, background='white')
drawpad.grid(row=0, column=1)

# Insert your code here to draw the house!

square = drawpad.create_rectangle(200,200,500,500, fill='green')
line1 = drawpad.create_line(350,100,200,200)
line2 = drawpad.create_line(350,100,500,200)
square2 = drawpad.create_rectangle(300,350,400,500, fill='red')
square3 = drawpad.create_rectangle(220,220,280,280, fill='red')
square4 = drawpad.create_rectangle(420,220,480,280, fill='red')
Circle = drawpad.create_oval(370,430,390,450, fill='dark red')
line5 = drawpad.create_line(400,140,400,100)
line6 = drawpad.create_line(400,100,480,100)
line7 = drawpad.create_line(480,100,480,190)
square5 = drawpad.create_rectangle(0,500,800,550, fill= 'dark green')
root.mainloop()
