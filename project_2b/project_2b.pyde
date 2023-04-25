#a Jigglypuff takes shelter and it and it's companions frantically spin from the impact of a bomb
#checklist: camera(done), translation/rotation(done), instancing(done), lighting(done), duration(done)
#Jigglypuff is replicated
#John Guner
from __future__ import division
import traceback

time = 0   # time is used to move objects from one frame to another
img = 0
def setup():
    size (800, 800, P3D)
    img = loadImage("space.jpg")
    try:
        frameRate(120)       # this seems to be needed to make sure the scene draws properly
        perspective (60 * PI / 180, 1, 0.1, 1000)  # 60-degree field of view
    except Exception:
        traceback.print_exc()

def draw():
    try:
        global time
        time += 0.01
        #camera motion
        camera(-45 + 10*10, -30, 150 - 10*2, 0, 0, 0, 0,  1, 0)
        if (time > 0 and time < 10):
            camera (-45 + time*10, -30, 150 - time*2, 0, 0, 0, 0,  1, 0)
            print(time)
        if (time > 10):
            camera (55 - time*10, -30, 130 + time*2, 0, 0, 0, 0,  1, 0)
            print(time)
        background (200, 200, 255)  # clear screen and set background to light blue
        
        # set up the lights
        ambientLight(50, 50, 50);
        lightSpecular(255, 255, 255)
        directionalLight (100, 100, 100, -0.3, 0.5, -1)
        
        #light source
        pointLight(51, 102, 126, width/2, height/2, 400)  
        
        # set some of the surface properties
        noStroke()
        specular (180, 180, 180)
        shininess (500)
        
        #instancing with method
        pushMatrix()
        if (time > 10):
            for i in range(4):
                rotateX(time)
                jigglypuff(20*i - 50, 8, -50)
        popMatrix()
        
        pushMatrix()
        if (time < 10):
            translate(0, 10*time, 0)
            bomb()
        popMatrix()   
         
        pushMatrix()
        if (time < 10):
            translate(0, 8, -time*19)
            jigglypuff(0, 0, 0)
        popMatrix()

        pushMatrix()
        if (time < 10):
            house()
        popMatrix()
        
        #grass
        fill (5, 255, 5)
        pushMatrix()
        translate (0, 29, 0)
        box(400, 1, 400)
        popMatrix()
        
        #duration 15 seconds
        if (time > 15):
            exit()
        
    except Exception:
        traceback.print_exc()

def jigglypuff(x, y, z):
    #head
    fill (255,170,255)
    pushMatrix()
    translate (0 + x, 8 + y, 80 + z)  # move up and down
    sphereDetail(10)  # this controls how many polygons make up each sphere
    sphere(5)
    popMatrix()
        
    #leg1
    fill (255,170,255)
    pushMatrix()
    translate (2 + x, 13 + y, 80 + z)
    sphere(2)
    popMatrix()
        
    #leg2
    fill (255,170,255)
    pushMatrix()
    translate (-2 + x, 13 + y, 80 + z)
    sphere(2)
    popMatrix()
        
    #arm1
    fill (255,170,255)
    pushMatrix()
    translate (5 + x, 8 + y, 80 + z)
    sphere(2)
    popMatrix()
        
    #arm2
    fill (255,170,255)
    pushMatrix()
    translate (-5 + x, 8 + y, 80 + z)
    sphere(2)
    popMatrix()
    
def bomb():
    fill (0, 0, 0)
    pushMatrix()
    translate (0, -100, 0)  # move up and down
    sphereDetail(60)  # this controls how many polygons make up each sphere
    sphere(20)
    popMatrix()
    
def house():
#sliding door divider
        fill (0, 0, 0)
        pushMatrix()
        
        translate (6, 15, -26)
        box(1, 20, 1.5)
        popMatrix()
        
        #sliding door part 1 
        fill (255, 255, 255)
        pushMatrix()
        
        translate (12.5, 15, -25)
        box(12.5, 20, 1)
        popMatrix()
        
        #sliding door part 2
        fill (255, 255, 255)
        pushMatrix()
        
        translate (-1, 15, -26)
        box(12.5, 20, 1)
        popMatrix()
        
        #garage door
        fill (25, 69, 42)
        pushMatrix()
        
        translate (-39.5, 15, 18.5)
        box(23, 23, 1)
        popMatrix()
        
        #garage window
        fill (255, 255, 255)
        pushMatrix()
        
        translate (-56, 12, 0)
        box(1, 13, 25)
        popMatrix()
        
        #garage base
        fill (130, 175, 175)
        pushMatrix()
        
        translate (-37.5, 8, 0)
        box(37.5, 37.5, 37.5)
        popMatrix()
        
        #side window
        fill (255, 255, 255)
        pushMatrix()
        
        translate (25, 12, 0)
        box(1, 13, 25)
        popMatrix()
        
        #front window 1
        fill (255, 255, 255)
        pushMatrix()
        
        translate (15, 12, 25)
        box(10, 13, 1)
        popMatrix()
        
        #front window 2
        fill (255, 255, 255)
        pushMatrix()
        
        translate (-15, 12, 25)
        box(10, 13, 1)
        popMatrix()
        
        #door knob
        fill (255, 255, 0)
        pushMatrix()
        
        translate (3.5, 14, 25)
        sphere(1)
        popMatrix()
        
        #front door
        fill (255, 0, 0)
        pushMatrix()
        
        translate (0, 15, 25)
        box(10, 20, 1)
        popMatrix()
        
        #base
        fill (128, 0, 0)
        pushMatrix()
        translate (0, -19, 0)
        box(65, 1, 65)
        popMatrix()
        
        #base
        fill (130, 175, 175)
        pushMatrix()
        translate (0, 4, 0)
        box(50, 45, 50)
        popMatrix()
        


# cylinder with radius = 1, z range in [-1,1]
def cylinder(sides = 50):
    # first endcap
    beginShape()
    for i in range(sides):
        theta = i * 2 * PI / sides
        x = cos(theta)
        y = sin(theta)
        vertex ( x,  y, -1)
    endShape(CLOSE)
    # second endcap
    beginShape()
    for i in range(sides):
        theta = i * 2 * PI / sides
        x = cos(theta)
        y = sin(theta)
        vertex ( x,  y, 1)
    endShape(CLOSE)
    # round main body
    x1 = 1
    y1 = 0
    for i in range(sides):
        theta = (i + 1) * 2 * PI / sides
        x2 = cos(theta)
        y2 = sin(theta)
        beginShape()
        normal (x1, y1, 0)
        vertex (x1, y1, 1)
        vertex (x1, y1, -1)
        normal (x2, y2, 0)
        vertex (x2, y2, -1)
        vertex (x2, y2, 1)
        endShape(CLOSE)
        x1 = x2
        y1 = y2
        
