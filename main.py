#OpenGL library import
import OpenGL
OpenGL.ERROR_ON_COPY = True

#For creating window
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

#Array of 4 tuple
fourTupleArray = []

#Height and width of the image
imageWidth = sys.argv[2]
imageHeight = sys.argv[3]

#Height and width of the window
windowWidth = int(sys.argv[4])
windowHeight = int(sys.argv[5])

#Function to initiate the 2D orthogonal window
def initiate2DWindow(r,g,b):
    #Clear buffer
    glClearColor(r,g,b,0.0)
    #Set 2D orthogonal window with specified width and height
    glMatrixMode (GL_PROJECTION)
    gluOrtho2D (0.0, float(imageWidth), 0.0, float(imageHeight))

def drawDragonAsPolygon():
    glColor3ub(255, 0, 0)
    glBegin(GL_POLYGON)
    for line in fourTupleArray:
        glVertex2i(line[0], int(imageHeight) - line[1])
        glVertex2i(line[2], int(imageHeight) - line[3])
    glEnd()

def drawDragonAsLines():
    #Set line color to red
    glColor3f(1.0, 0.0, 0.0)
    #Draw each line from array of points
    for line in fourTupleArray:
      #Line section begin
      glBegin(GL_LINES)
      #Set Point 1
      glVertex2i(line[0], int(imageHeight) - line[1])
      #Set Point 2
      glVertex2i(line[2], int(imageHeight) - line[3])
      #Line section end
      glEnd()

#Function to draw the display
def renderDisplay():
    #Clear buffer
    glClear(GL_COLOR_BUFFER_BIT)

    #Draw dragon
    drawDragonAsLines()

    #Draw line and flush the buffer
    glFlush()

#Function to read array of points from file
def readPointsFromFile():
    #File mode = read
    mode = 'r'
    #Open file
    with open(sys.argv[1], mode) as fileObject:
        #Read each line
        for line in fileObject:
            #Split line to space separated integer and insert the numbers to a temporary list
            temporaryList = [int(num) for num in line.split()]
            #Append the list to the main array
            fourTupleArray.append(temporaryList)

#Function to print the main array for debugging purpose
def printTupleArray():
    for line in fourTupleArray:
        print(line[0])
        print(line[1])
        print(line[2])
        print(line[3])
        print()

#Main program

#Read data from file
readPointsFromFile()
#Initiate glut windoe
glutInit(sys.argv)
#Set display mode to single using RGB coloring method
glutInitDisplayMode (GLUT_SINGLE | GLUT_RGB)
#Set initial window size to
glutInitWindowSize (windowWidth, windowHeight)
#Set initial window position to bottom left
glutInitWindowPosition (0, 0)
#Create window with desired name
glutCreateWindow (sys.argv[6])
#Pop the window
initiate2DWindow(0.0,0.0,0.0)
#Render the display
glutDisplayFunc(renderDisplay)
#Run glut main loop to keep the window open until it's closed
glutMainLoop()
