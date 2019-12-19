#2019-20 Fall Computer Science Principles Final Exam

#Ms. Haubold


#Name
#Adam Schmok
#Date
#12/19/2019


#### INSTRUCTIONS ####
#Create an etch a sketch turtle game
#The turtle should move with the arrow keys (up, down, left and right), and draw
#Space should clear the screen
#o and p should make the pen size bigger and smaller
#u should pick the pen up or put the pen down
#All code must be commented
#BONUS
#Add a feature to change colors
#

#import required libraries
import turtle #imports the turtle module

#create turtle
drawer = turtle.Turtle() #makes a turtle called "drawer"
drawer.resizemode("auto")
#make varaibles
switch = True #creates a varaible used to toggle the pen state
pen_size = 1 #makes a varaible used to change the size of the pen
#movement functions
def up(): #makes a function that moves the turtle up
    drawer.setheading(90) #makes turtle face up
    drawer.forward(10) #moves turtle forward 10 pixels

def right(): #makes a function that moves the turtle right
    drawer.setheading(0) #makes turtle face right
    drawer.forward(10) #moves turtle forward 10 pixels

def down(): #makes a function that moves the turtle down
    drawer.setheading(270) #makes turtle face down
    drawer.forward(10) #moves turtle forward 10 pixels

def left(): #makes a function that moves the turtle left
    drawer.setheading(180) #makes turtle face left
    drawer.forward(10) #moves turtle forward 10 pixels

def pen_change(): #toggles between writing and not writing
    global switch #makes switch variable accessible
    if switch: #checks to see if switch is true or false
        drawer.pu() #stops drawing
        switch = False #toggles switch
    else: #if switch is false, this code is executed
        drawer.pd() #starts drawing
        switch = True #toggles switch

def grow(): #makes the pen thickness bigger
    global pen_size #makes pen_size varaible accessible
    pen_size += 1 #adds 1 to the pen_size variable
    if pen_size > 100: #checks to see if the pen size will be bigger than 100
        pen_size = 100 #sets the pen thickness to 100
    drawer.pensize(pen_size) #updates the turtle's pen thickness

def shrink(): #makes the pen thickness smaller
    global pen_size #makes pen_size varaible accessible
    pen_size -= 1 #subtracts 1 from the pen_size variable
    if pen_size < 1: #checks to see if subtraction will result in zero or a negative number
        pen_size = 1 #sets the pen thickness to 1
    drawer.pensize(pen_size) #updates the turtle's pen thickness

def clear_screen(): #erases any drawings
    drawer.clear() #clears the screen of any writing

#color/drawing functions
def color_black(): #makes a function that changes the color of the pen to black
    drawer.color("black") #changes the pen's color to black

def color_red(): # makes a function that changes the color of the pen to red
    drawer.color("red") # changes the pen's color to red

def color_blue(): # makes a function that changes the color of the pen to blue
    drawer.color("blue") # changes the pen's color to blue

def color_green(): # makes a function that changes the color of the pen to green
    drawer.color("green") # changes the pen's color to green

def color_pink(): # makes a function that changes the color of the pen to pink
    drawer.color("pink") # changes the pen's color to pink

def color_purple(): # makes a function that changes the color of the pen to purple
    drawer.color("purple") # changes the pen's color to purple

def color_orange(): # makes a function that changes the color of the pen to orange
    drawer.color("orange") # changes the pen's color to orange

def color_gray(): # makes a function that changes the color of the pen to gray
    drawer.color("gray") # changes the pen's color to gray

def color_brown(): # makes a function that changes the color of the pen to brown
    drawer.color("brown") # changes the pen's color to brown

#create screen
wn = turtle.Screen() #creates a varaible to access the screen

#bind to keypresses 
wn.onkeypress(up, "Up") #binds function to move up to the up arrow
wn.onkeypress(right,"Right") #binds function to move right to the right arrow
wn.onkeypress(down,"Down") #binds function to move down to the down arrow
wn.onkeypress(left,"Left") #binds function to move left to the left arrow

wn.onkeyrelease(clear_screen,"space") #binds function to clear the screen to the space bar
wn.onkeyrelease(pen_change,"u") #binds function to toggle pen state to the u key
wn.onkeypress(grow,"o") #binds function to make pen thicker to the o key
wn.onkeypress(shrink,"p") #binds function to make pen thinner to the p key

wn.onkeyrelease(color_black,"1") #binds function to change color to black to 1 key
wn.onkeyrelease(color_red,"2") #binds function to change color to red to 2 key
wn.onkeyrelease(color_blue,"3") #binds function to change color to blue to 3 key
wn.onkeyrelease(color_green,"4") #binds function to change color to green to 4 key
wn.onkeyrelease(color_pink,"5") #binds function to change color to pink to 5 key
wn.onkeyrelease(color_purple,"6") #binds function to change color to purple to 6 key
wn.onkeyrelease(color_orange,"7") #binds function to change color to orange to 7 key
wn.onkeyrelease(color_gray,"8") #binds function to change color to gray to 8 key
wn.onkeyrelease(color_brown,"9") #binds function to change color to brown to 9 key
#listen
wn.listen() #begins to check for any key presses

#mainloop
wn.mainloop() #keeps the turtle screen active after all code is finished