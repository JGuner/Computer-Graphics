# Drawing Routines that are similar to those in OpenGL
#John Guner
from matrix_stack import *

vertices = []
toggle = -1
leftC = 0
rightC = 0
bottomC = 0
topC = 0
fovC = 0

def gtOrtho(left, right, bottom, top, near, far):
    global leftC, rightC, bottomC, topC, toggle
    toggle = 0
    leftC = float(left)
    rightC = float(right)
    bottomC = float(bottom)
    topC = float(top)
   
def gtPerspective(fov, near, far):
    global leftC, rightC, bottomC, topC, fovC, toggle
    toggle = 1
    fovC = float(math.radians(fov))
   
def gtVertex(x, y, z):
    global leftC, rightC, bottomC, topC, fovC, toggle
    stack = getStack()
    ctm = stack[-1]
    
    transform = gtMatMul(ctm, [[x],[y],[z],[1]])
    new_x = transform[0][0]
    new_y = transform[1][0]
    new_z = transform[2][0]
    
    if toggle == 0:
        x_prime = (new_x - leftC)*((width)/(rightC - leftC))
        y_prime = height-(new_y - bottomC)*((height)/(topC - bottomC))
        vertices.append([x_prime, y_prime])
        
    if toggle == 1:
        k = float(math.tan(fovC/2))
        x_prime = new_x/(abs(new_z))
        y_prime = new_y/(abs(new_z))
        x_final = (x_prime + k)*(width/(2*k))
        y_final = height-(y_prime + k)*(height/(2*k))
        vertices.append([x_final, y_final])
        
def gtBeginShape():
    global vertices
    vertices = []

def gtEndShape():
    for i in range(0, len(vertices)-1, 2):        
        line(vertices[i][0], vertices[i][1], vertices[i+1][0], vertices[i+1][1])
