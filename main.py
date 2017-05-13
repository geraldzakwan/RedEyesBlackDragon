#OpenGL library import
import OpenGL
OpenGL.ERROR_ON_COPY = True

#For creating window
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

#Array of 4 tuple
#array for:
fourTupleArrayR = []	#right wing
fourTupleArrayB = []	#body
fourTupleArrayL = []	#left wing
fourTupleArrayN = []	#neck
fourTupleArrayTA = []	#tails part a ...
fourTupleArrayTB = []
fourTupleArrayTC = []
fourTupleArrayTD = []
fourTupleArrayTE = []
fourTupleArrayTF = []
fourTupleArrayTG = []
fourTupleArrayH = []	#head
fourTupleArrayHA = []	#head fur a...
fourTupleArrayHB = []

fourTupleArray2 = []

#Height and width of the image
imageWidth = "1500"
imageHeight = "705"

#Height and width of the window
windowWidth = int(1500)
windowHeight = int(705)

#Function to initiate the 2D orthogonal window
def initiate2DWindow(r,g,b):
    #Clear buffer
    glClearColor(r,g,b,0.0)
    #Set 2D orthogonal window with specified width and height
    glMatrixMode (GL_PROJECTION)
    gluOrtho2D (0.0, float(imageWidth), 0.0, float(imageHeight))

def drawDragonAsPolygonR():
    glColor3ub(255, 0, 0)
    glBegin(GL_POLYGON)
    for line in fourTupleArrayR:
        glVertex2i(line[0], int(imageHeight) - line[1])
        glVertex2i(line[2], int(imageHeight) - line[3])
    glEnd()

def drawDragonAsPolygonB():
	glColor3ub(150, 0, 0)
	glBegin(GL_POLYGON)
	for line in fourTupleArrayB:
		glVertex2i(line[0], int(imageHeight) - line[1])
		glVertex2i(line[2], int(imageHeight) - line[3])
	glEnd()

def drawDragonAsPolygonL():
	glColor3ub(255, 0, 0)
	glBegin(GL_POLYGON)
	for line in fourTupleArrayL:
		glVertex2i(line[0], int(imageHeight) - line[1])
		glVertex2i(line[2], int(imageHeight) - line[3])
	glEnd()

def drawDragonAsPolygonN():
	glColor3ub(150, 0, 0)
	glBegin(GL_POLYGON)
	for line in fourTupleArrayN:
		glVertex2i(line[0], int(imageHeight) - line[1])
		glVertex2i(line[2], int(imageHeight) - line[3])
	glEnd()

def drawDragonAsPolygonTA():
	glColor3ub(150, 0, 0)
	glBegin(GL_POLYGON)
	for line in fourTupleArrayTA:
		glVertex2i(line[0], int(imageHeight) - line[1])
		glVertex2i(line[2], int(imageHeight) - line[3])
	glEnd()


def drawDragonAsPolygonTB():
	glColor3ub(150, 0, 0)
	glBegin(GL_POLYGON)
	for line in fourTupleArrayTB:
		glVertex2i(line[0], int(imageHeight) - line[1])
		glVertex2i(line[2], int(imageHeight) - line[3])
	glEnd()


def drawDragonAsPolygonTC():
	glColor3ub(150, 0, 0)
	glBegin(GL_POLYGON)
	for line in fourTupleArrayTC:
		glVertex2i(line[0], int(imageHeight) - line[1])
		glVertex2i(line[2], int(imageHeight) - line[3])
	glEnd()


def drawDragonAsPolygonTD():
	glColor3ub(150, 0, 0)
	glBegin(GL_POLYGON)
	for line in fourTupleArrayTD:
		glVertex2i(line[0], int(imageHeight) - line[1])
		glVertex2i(line[2], int(imageHeight) - line[3])
	glEnd()

def drawDragonAsPolygonTE():
	glColor3ub(150, 0, 0)
	glBegin(GL_POLYGON)
	for line in fourTupleArrayTE:
		glVertex2i(line[0], int(imageHeight) - line[1])
		glVertex2i(line[2], int(imageHeight) - line[3])
	glEnd()

def drawDragonAsPolygonTF():
	glColor3ub(150, 0, 0)
	glBegin(GL_POLYGON)
	for line in fourTupleArrayTF:
		glVertex2i(line[0], int(imageHeight) - line[1])
		glVertex2i(line[2], int(imageHeight) - line[3])
	glEnd()

def drawDragonAsPolygonTG():
	glColor3ub(150, 0, 0)
	glBegin(GL_POLYGON)
	for line in fourTupleArrayTG:
		glVertex2i(line[0], int(imageHeight) - line[1])
		glVertex2i(line[2], int(imageHeight) - line[3])
	glEnd()


def drawDragonAsPolygonH():
	glColor3ub(150, 0, 0)
	glBegin(GL_POLYGON)
	for line in fourTupleArrayH:
		glVertex2i(line[0], int(imageHeight) - line[1])
		glVertex2i(line[2], int(imageHeight) - line[3])
	glEnd()

def drawDragonAsPolygonHA():
	glColor3ub(150, 0, 0)
	glBegin(GL_POLYGON)
	for line in fourTupleArrayHA:
		glVertex2i(line[0], int(imageHeight) - line[1])
		glVertex2i(line[2], int(imageHeight) - line[3])
	glEnd()

def drawDragonAsPolygonHB():
	glColor3ub(150, 0, 0)
	glBegin(GL_POLYGON)
	for line in fourTupleArrayHB:
		glVertex2i(line[0], int(imageHeight) - line[1])
		glVertex2i(line[2], int(imageHeight) - line[3])
	glEnd()

def drawBackup1():
    glColor3ub(0, 0, 0)
    glBegin(GL_POLYGON)
    glVertex2i(719, 705-197)
    glVertex2i(690, 705-149)
    glVertex2i(579, 705-75)
    glVertex2i(633, 705-13)
    glEnd()

def drawBackup2():
    glColor3ub(0, 0, 0)
    glBegin(GL_POLYGON)
    glVertex2i(865, 705-15)
    glVertex2i(921, 705-65)
    glVertex2i(901, 705-147)
    glVertex2i(823, 705-195)
    glEnd()

def drawDragonAsLines():
    #Set line color to black
    glColor3f(255.0, 255.0, 255.0)
    #Draw each line from array of points
    glLineWidth(3.0)
    for line in fourTupleArray2:
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
    drawDragonAsPolygonR()
    drawDragonAsPolygonB()
    drawDragonAsPolygonL()
    drawDragonAsPolygonN()
    drawDragonAsPolygonTA()
    drawDragonAsPolygonTB()
    drawDragonAsPolygonTC()
    drawDragonAsPolygonTD()
    drawDragonAsPolygonTE()
    drawDragonAsPolygonTF()
    drawDragonAsPolygonTG()
    drawDragonAsPolygonH()
    drawDragonAsPolygonHA()
    drawDragonAsPolygonHB()
    drawBackup1()
    drawBackup2()
    drawDragonAsLines()

    #Draw line and flush the buffer
    glFlush()

#Function to read array of points from file
def readPointsFromFileRight():
    #File mode = read
    mode = 'r'
    #Open file
    with open("sampleDragon1rightwing", mode) as fileObject:
        #Read each line
        for line in fileObject:
            #Split line to space separated integer and insert the numbers to a temporary list
            temporaryList = [int(num) for num in line.split()]
            #Append the list to the main array
            fourTupleArrayR.append(temporaryList)

            #Function to read array of points from file

def readPointsFromFileBody():
    #File mode = read
    mode = 'r'
    #Open file
    with open("sampleDragon1body", mode) as fileObject:
        #Read each line
        for line in fileObject:
            #Split line to space separated integer and insert the numbers to a temporary list
            temporaryList = [int(num) for num in line.split()]
            #Append the list to the main array
            fourTupleArrayB.append(temporaryList)


            #Function to read array of points from file
def readPointsFromFileLeft():
    #File mode = read
    mode = 'r'
    #Open file
    with open("sampleDragon1leftwing", mode) as fileObject:
        #Read each line
        for line in fileObject:
            #Split line to space separated integer and insert the numbers to a temporary list
            temporaryList = [int(num) for num in line.split()]
            #Append the list to the main array
            fourTupleArrayL.append(temporaryList)

#Function to read array of points from file
def readPointsFromFileN():
    #File mode = read
    mode = 'r'
    #Open file
    with open("sampleDragon1neck", mode) as fileObject:
        #Read each line
        for line in fileObject:
            #Split line to space separated integer and insert the numbers to a temporary list
            temporaryList = [int(num) for num in line.split()]
            #Append the list to the main array
            fourTupleArrayN.append(temporaryList)

            #Function to read array of points from file

  #Function to read array of points from file
def readPointsFromFileTA():
    #File mode = read
    mode = 'r'
    #Open file
    with open("sampleDragon1taila", mode) as fileObject:
        #Read each line
        for line in fileObject:
            #Split line to space separated integer and insert the numbers to a temporary list
            temporaryList = [int(num) for num in line.split()]
            #Append the list to the main array
            fourTupleArrayTA.append(temporaryList)

  #Function to read array of points from file
def readPointsFromFileTB():
    #File mode = read
    mode = 'r'
    #Open file
    with open("sampleDragon1tailb", mode) as fileObject:
        #Read each line
        for line in fileObject:
            #Split line to space separated integer and insert the numbers to a temporary list
            temporaryList = [int(num) for num in line.split()]
            #Append the list to the main array
            fourTupleArrayTB.append(temporaryList)


  #Function to read array of points from file
def readPointsFromFileTC():
    #File mode = read
    mode = 'r'
    #Open file
    with open("sampleDragon1tailc", mode) as fileObject:
        #Read each line
        for line in fileObject:
            #Split line to space separated integer and insert the numbers to a temporary list
            temporaryList = [int(num) for num in line.split()]
            #Append the list to the main array
            fourTupleArrayTC.append(temporaryList)

  #Function to read array of points from file
def readPointsFromFileTD():
    #File mode = read
    mode = 'r'
    #Open file
    with open("sampleDragon1taild", mode) as fileObject:
        #Read each line
        for line in fileObject:
            #Split line to space separated integer and insert the numbers to a temporary list
            temporaryList = [int(num) for num in line.split()]
            #Append the list to the main array
            fourTupleArrayTD.append(temporaryList)


  #Function to read array of points from file
def readPointsFromFileTE():
    #File mode = read
    mode = 'r'
    #Open file
    with open("sampleDragon1taile", mode) as fileObject:
        #Read each line
        for line in fileObject:
            #Split line to space separated integer and insert the numbers to a temporary list
            temporaryList = [int(num) for num in line.split()]
            #Append the list to the main array
            fourTupleArrayTE.append(temporaryList)

  #Function to read array of points from file
def readPointsFromFileTF():
    #File mode = read
    mode = 'r'
    #Open file
    with open("sampleDragon1tailf", mode) as fileObject:
        #Read each line
        for line in fileObject:
            #Split line to space separated integer and insert the numbers to a temporary list
            temporaryList = [int(num) for num in line.split()]
            #Append the list to the main array
            fourTupleArrayTF.append(temporaryList)


  #Function to read array of points from file
def readPointsFromFileTG():
    #File mode = read
    mode = 'r'
    #Open file
    with open("sampleDragon1tailg", mode) as fileObject:
        #Read each line
        for line in fileObject:
            #Split line to space separated integer and insert the numbers to a temporary list
            temporaryList = [int(num) for num in line.split()]
            #Append the list to the main array
            fourTupleArrayTG.append(temporaryList)


def readPointsFromFileH():
    #File mode = read
    mode = 'r'
    #Open file
    with open("sampleDragon1head", mode) as fileObject:
        #Read each line
        for line in fileObject:
            #Split line to space separated integer and insert the numbers to a temporary list
            temporaryList = [int(num) for num in line.split()]
            #Append the list to the main array
            fourTupleArrayH.append(temporaryList)

def readPointsFromFileHA():
    #File mode = read
    mode = 'r'
    #Open file
    with open("sampleDragon1ha", mode) as fileObject:
        #Read each line
        for line in fileObject:
            #Split line to space separated integer and insert the numbers to a temporary list
            temporaryList = [int(num) for num in line.split()]
            #Append the list to the main array
            fourTupleArrayHA.append(temporaryList)

def readPointsFromFileHB():
    #File mode = read
    mode = 'r'
    #Open file
    with open("sampleDragon1hb", mode) as fileObject:
        #Read each line
        for line in fileObject:
            #Split line to space separated integer and insert the numbers to a temporary list
            temporaryList = [int(num) for num in line.split()]
            #Append the list to the main array
            fourTupleArrayHB.append(temporaryList)

def readPointsFromFile2():
    #File mode = read
    mode = 'r'
    #Open file
    with open("sampleDragon1", mode) as fileObject:
        #Read each line
        for line in fileObject:
            #Split line to space separated integer and insert the numbers to a temporary list
            temporaryList = [int(num) for num in line.split()]
            #Append the list to the main array
            fourTupleArray2.append(temporaryList)

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
readPointsFromFile2()
readPointsFromFileRight()
readPointsFromFileLeft()
readPointsFromFileBody()
readPointsFromFileN()
readPointsFromFileTA()
readPointsFromFileTB()
readPointsFromFileTC()
readPointsFromFileTD()
readPointsFromFileTE()
readPointsFromFileTF()
readPointsFromFileTG()
readPointsFromFileH()
readPointsFromFileHA()
readPointsFromFileHB()
#Initiate glut windoe
glutInit(sys.argv)
#Set display mode to single using RGB coloring method
glutInitDisplayMode (GLUT_SINGLE | GLUT_RGB)
#Set initial window size to
glutInitWindowSize (windowWidth, windowHeight)
#Set initial window position to bottom left
glutInitWindowPosition (0, 0)
#Create window with desired name
glutCreateWindow ("Grafika Ilustrasi Naga")
#Pop the window
initiate2DWindow(0.0,0.0,0.0)
#Render the display
glutDisplayFunc(renderDisplay)
#Run glut main loop to keep the window open until it's closed
glutMainLoop()
