# Provided code for Subdivison and Geodesic Spheres
from __future__ import division
import traceback

# parameters used for object rotation by mouse
mouseX_old = 0
mouseY_old = 0
rot_mat = PMatrix3D()
vTable = []
gTable = []
oTable = {}
currentCorner = 0
currentCornerVisible = False
showRandomColors = False

def nextCorner(cornerNum):
    triangleNum = cornerNum // 3
    return (3 * triangleNum + ((cornerNum + 1) % 3))

def previousCorner(cornerNum):
    triangleNum = cornerNum // 3
    return (3 * triangleNum + ((cornerNum - 1) % 3))

def oppositeCorner(cornerNum):
    return oTable.get(cornerNum)

def swingCorner(cornerNum):
    return nextCorner(oppositeCorner(nextCorner(cornerNum)))

def computeOTable(G, V):
    global oTable
    triplet = []
    oTable = {}
    for i in range(len(V)):
        triplet.append([min(V[nextCorner(i)], V[previousCorner(i)]), max(V[nextCorner(i)], V[previousCorner(i)]), i])
    triplet.sort()
    for j in range(0, len(triplet), 2):
        cornerA = triplet[j][2]
        cornerB = triplet[j+1][2]
        oTable[cornerA] = cornerB
        oTable[cornerB] = cornerA
        
def inflate():
    global gTable
    tempTable = []
    for i in range(len(gTable)):
        temp = PVector(gTable[i][0], gTable[i][1], gTable[i][2])
        temp.normalize()
        tempArray = [temp.x, temp.y, temp.z]
        tempTable.append(tempArray)
    gTable = tempTable
            
def subD():
        global vTable, gTable, oTable
        print(oTable)
        tempgTable = gTable
        tempvTable = []
        midpoints = {}
        for a, b in oTable.items():
            print(a)
            print(b)
            endpoint1 = gTable[vTable[previousCorner(a)]]
            endpoint2 = gTable[vTable[nextCorner(a)]]
            print("endpoint1" + str(endpoint1))
            print("endpoint2" + str(endpoint2))
            sum = []
            sum.append(endpoint1[0] + endpoint2[0])
            sum.append(endpoint1[1] + endpoint2[1])
            sum.append(endpoint1[2] + endpoint2[2])
            print("1st sum" + str(sum))
            sum[0] = sum[0] * (1/2)
            sum[1] = sum[1] * (1/2)
            sum[2] = sum[2] * (1/2)
            print("midpoint" + str(sum))
            midpoint = sum
            midpointIndex = len(tempgTable)
            tempgTable.append(midpoint)
            midpoints[a] = midpointIndex
            midpoints[b] = midpointIndex
        for x in range(0, len(vTable), 3):
            y = x + 1
            z = x + 2
            tempvTable.extend((vTable[x], midpoints[z], midpoints[y]))
            tempvTable.extend((midpoints[z], vTable[y], midpoints[x]))
            tempvTable.extend((midpoints[y], midpoints[x], vTable[z]))
            tempvTable.extend((midpoints[x], midpoints[y], midpoints[z]))
        gTable, vTable = tempgTable, tempvTable

# initalize things
def setup():
    size (800, 800, OPENGL)
    frameRate(30)
    noStroke()

# draw the current mesh (you will modify parts of this routine)
def draw():
    global showRandomColors, currentCornerVisible, gTable, vTable, oTable
    randomSeed(0)
    background (100, 100, 180)    # clear the screen to black

    perspective (PI*0.2, 1.0, 0.01, 1000.0)
    camera (0, 0, 6, 0, 0, 0, 0, 1, 0)    # place the camera in the scene
    
    # create an ambient light source
    ambientLight (102, 102, 102)

    # create two directional light sources
    lightSpecular (202, 202, 202)
    directionalLight (100, 100, 100, -0.7, -0.7, -1)
    directionalLight (152, 152, 152, 0, 0, -1)
    
    pushMatrix();

    stroke (0)                    # draw polygons with black edges
    fill (200, 200, 200)          # set the polygon color to white
    ambient (200, 200, 200)
    specular (0, 0, 0)            # turn off specular highlights
    shininess (1.0)
    
    applyMatrix (rot_mat)   # rotate the object using the global rotation matrix

    # THIS IS WHERE YOU SHOULD DRAW YOUR MESH
    for c in range(0, len(vTable), 3):
        beginShape()
        if showRandomColors:
            fill(random(255), random(255), random(255))
        else:
            fill(255, 255, 255)
        vertex(gTable[vTable[c]][0], gTable[vTable[c]][1], gTable[vTable[c]][2])
        vertex(gTable[vTable[c+1]][0], gTable[vTable[c+1]][1], gTable[vTable[c+1]][2])
        vertex(gTable[vTable[c+2]][0], gTable[vTable[c+2]][1], gTable[vTable[c+2]][2])
        endShape(CLOSE)
        if currentCornerVisible:
            pushMatrix()
            next = gTable[vTable[nextCorner(currentCorner)]]
            prev = gTable[vTable[previousCorner(currentCorner)]]
            curr = gTable[vTable[currentCorner]]
            mid = [(next[0] + prev[0]) / 2, (next[1] + prev[1]) / 2, (next[2] + prev[2]) / 2]
            cornerCircle = [curr[0] * .9 + mid[0] * .1, curr[1] * .9 + mid[1] * .1, curr[2] * .9 + mid[2] * .1]
            translate(cornerCircle[0], cornerCircle[1], cornerCircle[2])
            noStroke()
            fill(200, 0, 0)
            sphere(0.07)
            stroke(0)
            popMatrix()
    popMatrix()
    

# read in a mesh file (this needs to be modified)
def read_mesh(filename):
    global gTable, vTable, oTable
    gTable = []
    vTable = []
    oTable = {}
    fname = "data/" + filename
    # read in the lines of a file
    with open(fname) as f:
        lines = f.readlines()

    # determine number of vertices (on first line)
    words = lines[0].split()
    num_vertices = int(words[1])
    print "number of vertices =", num_vertices

    # determine number of faces (on first second)
    words = lines[1].split()
    num_faces = int(words[1])
    print "number of faces =", num_faces

    # read in the vertices
    for i in range(num_vertices):
        words = lines[i+2].split()
        x = float(words[0])
        y = float(words[1])
        z = float(words[2])
        print "vertex: ", x, y, z
        v = [x, y, z]
        gTable.append(v)
    print(gTable)
    # read in the faces
    for i in range(num_faces):
        j = i + num_vertices + 2
        words = lines[j].split()
        nverts = int(words[0])
        if (nverts != 3):
            print "error: this face is not a triangle"
            exit()

        index1 = int(words[1])
        index2 = int(words[2])
        index3 = int(words[3])
        print "triangle: ", index1, index2, index3
        vTable.append(index1)
        vTable.append(index2)
        vTable.append(index3)
    print(vTable)
    computeOTable(gTable, vTable)
    print(oTable)
# make sure proper error messages get reported when handling key presses
def keyPressed():
    try:
        handleKeyPressed()
    except Exception:
        traceback.print_exc()

# process key presses (call your own routines!)
def handleKeyPressed():
    global showRandomColors, currentCornerVisible, currentCorner
    if key == '1':
        read_mesh ('tetra.ply')
    elif key == '2':
        read_mesh ('octa.ply')
    elif key == '3':
        read_mesh ('icos.ply')
    elif key == '4':
        read_mesh ('star.ply')
    elif key == 'n': # next
        currentCorner = nextCorner(currentCorner)
    elif key == 'p': # previous
        currentCorner = previousCorner(currentCorner)
    elif key == 'o': # opposite
        currentCorner = oppositeCorner(currentCorner)
    elif key == 's': # swing
        currentCorner = swingCorner(currentCorner)
    elif key == 'd': # subdivide mesh
        subD()
        computeOTable(gTable, vTable)
    elif key == 'i': # inflate mesh
        inflate()
    elif key == 'r': # toggle random colors
        showRandomColors = not showRandomColors
    elif key == 'c': # toggle showing current corner
        currentCornerVisible = not currentCornerVisible
    elif key == 'q': # quit the program
        exit()

# remember where the user first clicked
def mousePressed():
    global mouseX_old, mouseY_old
    mouseX_old = mouseX
    mouseY_old = mouseY

# change the object rotation matrix while the mouse is being dragged
def mouseDragged():
    global rot_mat
    global mouseX_old, mouseY_old
    
    if (not mousePressed):
        return
    
    dx = mouseX - mouseX_old
    dy = mouseY - mouseY_old
    dy *= -1

    len = sqrt (dx*dx + dy*dy)
    if (len == 0):
        len = 1
    
    dx /= len
    dy /= len
    rmat = PMatrix3D()
    rmat.rotate (len * 0.005, dy, dx, 0)
    rot_mat.preApply (rmat)

    mouseX_old = mouseX
    mouseY_old = mouseY


    
