# John Guner
# This is the provided code for the ray tracing project.
# The most important part of this code is the command interpreter, which
# parses the scene description (.cli) files.

from __future__ import division
from helper_functions import *
import traceback

objects = []
light = []
vertices = []
u = PVector(0, 0, 0)
vc = PVector(0, 0, 0)
w = PVector(0, 0, 0)
fov = 0
backgroundColor = (0, 0, 0)
diffuseColor = (0, 0, 0)
ambientColor = (0, 0, 0)
specularColor = (0, 0, 0)
spec_power = 0
k_refl = 0
maxrecurse = 10
eyePos = PVector(0, 0, 0)
debug_flag = False   # print debug information when this is True

def setup():
    size(320, 320) 
    noStroke()
    colorMode(RGB, 1.0)  # Processing color values will be in [0, 1]  (not 255)
    background(0, 0, 0)
    frameRate(30)

# make sure proper error messages get reported when handling key presses
def keyPressed():
    try:
        handleKeyPressed()
    except Exception:
        traceback.print_exc()

# read and interpret a scene description .cli file based on which key has been pressed
def handleKeyPressed():
    if key == '1':
        interpreter("01_one_sphere.cli")
    elif key == '2':
        interpreter("02_three_spheres.cli")
    elif key == '3':
        interpreter("03_shiny_sphere.cli")
    elif key == '4':
        interpreter("04_many_spheres.cli")
    elif key == '5':
        interpreter("05_one_triangle.cli")
    elif key == '6':
        interpreter("06_icosahedron_and_sphere.cli")
    elif key == '7':
        interpreter("07_colorful_lights.cli")
    elif key == '8':
        interpreter("08_reflective_sphere.cli")
    elif key == '9':
        interpreter("09_mirror_spheres.cli")
    elif key == '0':
        interpreter("10_reflections_in_reflections.cli")
    elif key == '-':
        interpreter("11_star.cli")

# You should add code for each command that calls routines that you write.
# Some of the commands will not be used until Part B of this project.
def interpreter(fname):
    global objects
    global light
    global vertices
    global u
    global vc
    global w
    global fov
    global backgroundColor
    global ambientColor
    global specularColor
    global diffuseColor
    global spec_power
    global k_refl
    global eyePos
    reset_scene()  # you should initialize any data structures that you will use here
    
    fname = "data/" + fname
    # read in the lines of a file
    with open(fname) as f:
        lines = f.readlines()

    # parse the lines in the file in turn
    for line in lines:
        words = line.split()  # split up the line into individual tokens
        if len(words) == 0:   # skip empty lines
            continue
        if words[0] == 'sphere':
            x = float(words[2])
            y = float(words[3])
            z = float(words[4])
            radius = float(words[1])
            v = PVector(x, y, z)
            # call your sphere making routine here
            # for example: create_sphere(x,y,z,radius)
            tempObject = Sphere(radius, x, y, z, diffuseColor[0], diffuseColor[1], diffuseColor[2],
                                ambientColor [0], ambientColor[1], ambientColor[2],
                                specularColor[0], specularColor[1], specularColor[2], spec_power, k_refl)
            objects.append(tempObject)
            
        elif words[0] == 'fov':
            fov = float(words[1])
            
        elif words[0] == 'eye':
            ex = float(words[1])
            ey = float(words[2])
            ez = float(words[3])
            eyePos = PVector(ex, ey, ez)
            
        elif words[0] == 'uvw':
            ux = float(words[1])
            uy = float(words[2])
            uz = float(words[3])
            vx = float(words[4])
            vy = float(words[5])
            vz = float(words[6])
            wx = float(words[7])
            wy = float(words[8])
            wz = float(words[9])
            u = PVector(ux, uy, uz)
            vc = PVector(vx, vy, vz)
            w = PVector(wx, wy, wz)

        elif words[0] == 'background':
            r = float(words[1])
            g = float(words[2])
            b = float(words[3])
            backgroundColor = (r, g, b)
            
        elif words[0] == 'light':
            x = float(words[1])
            y = float(words[2])
            z = float(words[3])
            r = float(words[4])
            g = float(words[5])
            b = float(words[6])
            v = PVector(x, y, z)
            lightObject = Light(v, r, g, b)
            light.append(lightObject)
            
        elif words[0] == 'surface':
            dr = float(words[1])
            dg = float(words[2])
            db = float(words[3])
            diffuseColor = (dr, dg, db)
            
            ar = float(words[4])
            ag = float(words[5])
            ab = float(words[6])
            ambientColor = (ar, ag, ab)
            
            sr = float(words[7])
            sg = float(words[8])
            sb = float(words[9])
            specularColor = (sr, sg, sb)
            
            spec_power = float(words[10])
            k_refl = float(words[11])
            
        elif words[0] == 'begin':
            vertices = []
            
        elif words[0] == 'vertex':
            vertices.append(PVector(float(words[1]), float(words[2]), float(words[3])))
            
        elif words[0] == 'end':
            objects.append(Triangle(vertices[0], vertices[1], vertices[2], diffuseColor[0], diffuseColor[1], diffuseColor[2],
                                ambientColor [0], ambientColor[1], ambientColor[2],
                                specularColor[0], specularColor[1], specularColor[2], spec_power, k_refl))
        elif words[0] == 'render':
            render_scene()    # render the scene (this is where most of the work happens)
        elif words[0] == '#':
            pass  # ignore lines that start with the comment symbol (pound-sign)
        else:
            print ("unknown command: " + word[0])

# render the ray tracing scene
def render_scene():
    global objects
    global light
    global vertices
    global u
    global vc
    global w
    global fov
    global backgroundColor
    global ambientColor
    global specularColor
    global diffuseColor
    global spec_power
    global k_refl
    global eyePos
    global debug_flag

    
    d = 1/tan(radians(fov/2))
    
    #y axis is pointing down when positive
        
    for j in range(height):
        for i in range(width):
            ux = ((2*i) / width) - 1
            vx = ((2*j) / height) - 1
          
            if i == 165 and j == 195:
                debug_flag = True
            else:
                debug_flag = False
            ray = Ray(PVector(eyePos.x, eyePos.y, eyePos.z), ((w * -d) + (u * (-1 + 2 * i / width)) + (vc * (-1 + 2 * j / height))).normalize())
            
            hits = []
            for o in objects:
                curr = o.getIntersect(ray)
                if curr != None:
                    dist = PVector.dist(curr, ray.origin)
                    hits.append((dist, curr, o))            
            #check if there are no hits and set to background color
            if len(hits) == 0:
                pix_color = color(backgroundColor[0], backgroundColor[1], backgroundColor[2])
                set(i, height-j, pix_color)
            else:
                nearestPoints, o = min(hits)[1:3]
                newColor = get_Color(ray, o, nearestPoints, 10)
                pix_color = color(*newColor)
                set(i,height-j, pix_color)


def get_Color(ray, object, point, max_depth):
    global objects
    global light
    global vertices
    global u
    global vc
    global w
    global fov
    global backgroundColor
    global ambientColor
    global specularColor
    global diffuseColor
    global spec_power
    global k_refl
    global eyePos
    global maxrecurse
    global debug_flag
    
    final_color = [0, 0, 0]
    
    if isinstance(object, Sphere):
        surf_norm = (point - object.center).normalize()
    else:
        surf_norm = object.triNorm
        if PVector.dot(surf_norm, ray.direction) >= 0:
           surf_norm = (object.triNorm * -1)

    for l in light:
        shadowCover = False
        lightVector = (l.v - point).normalize()
        if isinstance(object, Sphere) or isinstance(object, Triangle):
                    for curr in objects:
                        
                        offset = surf_norm * (.0001)
                        shadowrayOrigin = point + offset
                        shadowrayDirection = (l.v - point).normalize()

                        
                        hit = curr.getIntersect(Ray(shadowrayOrigin, shadowrayDirection))
                        
                        if debug_flag:
                            print "checking shadow for light with position: ", l.v
                            print "hit position: ", point
                            print "shadow ray origin (should be the hit position slightly offset away from the surface): ", shadowrayOrigin 
                            print "shadow ray direction: ", shadowrayDirection
                            print "shadow hit: ", hit
                            print "distance from light to original hit:", PVector.dist(l.v, point)
                            print ""
                        
                        if isinstance(curr, Sphere):
                            if hit != None and (PVector.dist(l.v, curr) < PVector.dist(point, l.v)):
                                shadowCover = True
                        elif isinstance(object, Triangle):
                            t = PVector.dot(object.triNorm, (object.a - shadowrayOrigin)) / (PVector.dot(object.triNorm, shadowrayDirection))
                            if hit != None and (t < PVector.dist(point, l.v)):
                                shadowCover = True
        
        if shadowCover == False:                      
            diffuseCoeff = max(PVector.dot(surf_norm, lightVector), 0)
            final_color[0] += object.dr * l.r * diffuseCoeff
            final_color[1] += object.dg * l.g * diffuseCoeff
            final_color[2] += object.db * l.b * diffuseCoeff
            
            L = (l.v - point)
            D = (point - ray.origin)
            H = (L - D).normalize()
            specCoeff = PVector.dot(H, surf_norm)**object.spec_power

            final_color[0] += object.sr * l.r * specCoeff
            final_color[1] += object.sg * l.g * specCoeff
            final_color[2] += object.sb * l.b * specCoeff    
            
    final_color[0] += object.ar
    final_color[1] += object.ag
    final_color[2] += object.ab
    
    if object.k_refl > 0 and max_depth > 0:
        reflectionrayOrigin = point + surf_norm * (0.0001)
        reflectionrayDirection = (ray.direction + (2 * (PVector.dot(surf_norm, (ray.direction * -1)))) * surf_norm).normalize()
        reflectionRay = Ray(reflectionrayOrigin, reflectionrayDirection)
        reflectionHits = []
        # if debug_flag:
        #     print "current hit is: ", point
        #     print "reflection ray origin (should be the hit position slightly offset away from the surface): ", reflectionrayOrigin 
        #     print "R (reflection ray direction): ", reflectionrayDirection
        for o in objects:
            if o == object:
                continue
            currIntersect = o.getIntersect(reflectionRay)
            print(currIntersect)
            #same logic as before check for the hits and append them to the list of hits
            if currIntersect != None:
                if o.t > 0:
                    dist = PVector.dist(currIntersect, point)
                    #get closest point later on by using min
                    reflectionHits.append((dist, o, currIntersect))
        if len(reflectionHits) > 0:
            nearestObject = min(reflectionHits)
            # reflectionRay nearestObject:object nearestObject:point
            recursiveShading = get_Color(reflectionRay, nearestObject[1], nearestObject[2], max_depth - 1)
            final_color[0] += object.k_refl * recursiveShading[0]
            final_color[1] += object.k_refl * recursiveShading[1]
            final_color[2] += object.k_refl * recursiveShading[2]
        else:   
            final_color[0] += object.k_refl * backgroundColor[0]
            final_color[1] += object.k_refl * backgroundColor[1]
            final_color[2] += object.k_refl * backgroundColor[2]
    
    return final_color

# here you should reset any data structures that you will use for your scene (e.g. list of spheres)
def reset_scene():
    global objects
    global light
    global vertices
    global u
    global vc
    global w
    global fov
    global backgroundColor
    global ambientColor
    global specularColor
    global diffuseColor
    global spec_power
    global k_refl
    global eyePos

    objects = []
    light = []
    vertices = []
    u = PVector(0, 0, 0)
    vc = PVector(0, 0, 0)
    w = PVector(0, 0, 0)
    fov = 0
    backgroundColor = (0, 0, 0)
    diffuseColor = (0, 0, 0)
    ambientColor = (0, 0, 0)
    specularColor = (0, 0, 0)
    spec_power = 0
    k_refl = 0
    eyePos = PVector(0, 0, 0)
    
# prints mouse location clicks, for help debugging
def mousePressed():
    print ("You pressed the mouse at " + str(mouseX) + " " + str(mouseY))

# this function should remain empty for this assignment
def draw():
    pass
