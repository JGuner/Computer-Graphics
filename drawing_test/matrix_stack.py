# Your Matrix Stack Library
#John Guner
import math
global ctm
stack = []

# you should modify the provided empty routines to complete the assignment

def gtInitialize():
    global stack
    stack = []
    identity = [[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]]
    stack.append(identity)
    
def gtPopMatrix():
    global stack
    stack.pop()

def gtPushMatrix():
    global stack
    ctm = stack[-1]
    dupe = [x[:] for x in ctm]
    stack.append(dupe)
    
def gtMatMul(m1, m2):
    return [
        [sum(x * y for x, y in zip(m1_r, m2_c)) for m2_c in zip(*m2)] for m1_r in m1
    ]

def gtScale(x,y,z):
    global stack
    ctm = stack[-1]
    scaleMat = [[x, 0, 0, 0], 
                [0, y, 0, 0], 
                [0, 0, z, 0], 
                [0, 0, 0, 1]]
    stack[-1] = (gtMatMul(ctm, scaleMat))

def gtTranslate(x,y,z):
    global stack
    ctm = stack[-1]
    transMat = [[1, 0, 0, x], 
                [0, 1, 0, y], 
                [0, 0, 1, z], 
                [0, 0, 0, 1]]
    stack[-1] = ((gtMatMul(ctm, transMat)))
    
def gtRotateX(theta):
    global stack
    rad = theta * (math.pi / 180)
    ctm = stack[-1]
    rotX = [[1, 0, 0, 0], 
            [0, math.cos(rad), -(math.sin(rad)), 0], 
            [0, math.sin(rad), math.cos(rad), 0], 
            [0, 0, 0, 1]]
    stack[-1] = ((gtMatMul(ctm, rotX)))
    
def gtRotateY(theta):
    rad = theta * (math.pi / 180)
    ctm = stack[-1]
    rotY = [[math.cos(rad), 0, math.sin(rad), 0], 
            [0, 1, 0, 0], 
            [-(math.sin(rad)), 0, math.cos(rad), 0], 
            [0, 0, 0, 1]]
    stack[-1] = ((gtMatMul(ctm, rotY)))

def gtRotateZ(theta):
    global stack
    rad = theta * (math.pi / 180)
    ctm = stack[-1]
    rotZ = [[math.cos(rad), -(math.sin(rad)), 0, 0], 
            [math.sin(rad), math.cos(rad), 0, 0], 
            [0, 0, 1, 0], 
            [0, 0, 0, 1]]
    stack[-1] = ((gtMatMul(ctm, rotZ)))
    
def print_ctm():
    global stack
    if stack:
        for i in range(len(stack[-1])):
            print(stack[-1][i])
    print("\n")

def getStack():
    global stack
    return stack
