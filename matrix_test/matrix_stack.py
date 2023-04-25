# Your Matrix Stack Library
import math
global ctm
global stack
# you should modify the provided empty routines to complete the assignment

def gtInitialize():
    global stack
    stack = []
    identity = [[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]]
    stack.append(identity)
    
def gtPopMatrix():
    stack.pop()

def gtPushMatrix():
    ctm = stack[-1]
    dupe = [x[:] for x in ctm]
    stack.append(dupe)
    
def gtMatMul(a, b):
    ans = [[0 for x in range(4)] for y in range(4)]
    for i in range(4):
        for j in range(4):
            for k in range(4):
                ans[i][j] += a[i][k] * b[k][j]
    return ans

def gtScale(x,y,z):
    ctm = stack[-1]
    scaleMat = [[x, 0, 0, 0], 
                [0, y, 0, 0], 
                [0, 0, z, 0], 
                [0, 0, 0, 1]]
    stack.append(gtMatMul(ctm, scaleMat))

def gtTranslate(x,y,z):
    ctm = stack[-1]
    transMat = [[1, 0, 0, x], 
                [0, 1, 0, y], 
                [0, 0, 1, z], 
                [0, 0, 0, 1]]
    stack.append((gtMatMul(ctm, transMat)))
    
def gtRotateX(theta):
    rad = theta * (math.pi / 180)
    ctm = stack[-1]
    rotX = [[1, 0, 0, 0], 
            [0, math.cos(rad), -(math.sin(rad)), 0], 
            [0, math.sin(rad), math.cos(rad), 0], 
            [0, 0, 0, 1]]
    stack.append((gtMatMul(ctm, rotX)))
    
def gtRotateY(theta):
    rad = theta * (math.pi / 180)
    ctm = stack[-1]
    rotY = [[math.cos(rad), 0, math.sin(rad), 0], 
            [0, 1, 0, 0], 
            [-(math.sin(rad)), 0, math.cos(rad), 0], 
            [0, 0, 0, 1]]
    stack.append((gtMatMul(ctm, rotY)))

def gtRotateZ(theta):
    rad = theta * (math.pi / 180)
    ctm = stack[-1]
    rotZ = [[math.cos(rad), -(math.sin(rad)), 0, 0], 
            [math.sin(rad), math.cos(rad), 0, 0], 
            [0, 0, 1, 0], 
            [0, 0, 0, 1]]
    stack.append((gtMatMul(ctm, rotZ)))

def print_ctm():
    global stack
    if stack:
        for i in range(len(stack[-1])):
            print(stack[-1][i])
    print("\n")
