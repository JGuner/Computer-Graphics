# The routine below should draw your initials in perspective
#John Guner
from matrix_stack import *
from drawlib import *

def persp_initials():
    gtInitialize()
    gtPerspective (100, -100, 100)
    gtPushMatrix()
    gtTranslate(1, 0, -4)
    JOHNGUNER()
    gtPopMatrix()
    
def JOHNGUNER():
    gtBeginShape()
    
    gtVertex (-2.0, 1.0,  -1.0)
    gtVertex (0.0,  1.0,  -1.0)

    gtVertex (-1.0,  1.0,  -1.0)
    gtVertex (-1.0,  0.0,  0.0)
    
    gtVertex ( -1.0,  0.0,  0.0)
    gtVertex ( -2.0, 0.0,  0.0)
    
    gtVertex ( -2.0, 0.0,  0.0)
    gtVertex ( -2.0, .25,  -.25)
    
    gtVertex ( -1.0,  0.0,  0.0)
    gtVertex ( 0.0, 0.0,  0.0)
    
    gtVertex ( -1.0,  0.0,  0.0)
    gtVertex ( -1.0, -1.0,  1.0)
    
    gtVertex ( -1.0,  -1.0,  1.0)
    gtVertex ( 0.0, -1.0,  1.0)
    
    gtVertex ( 0.0,  -1.0,  1.0)
    gtVertex ( 0.0, -0.5,  0.5)
    
    gtVertex ( 0.0,  -0.5,  0.5)
    gtVertex ( -.25, -0.5,  0.5)
    
    gtEndShape()   
