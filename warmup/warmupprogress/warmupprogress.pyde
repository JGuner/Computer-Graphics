width = 600
center = width/2.0

#s = (width / 2 - mouseX)
def setup():
    size(width, width)
def center_square(x,y,w):
    if x < 200:
        fill(200, 150, 69)
    elif x < 400:
        fill(69, 69, 69)
    else:
        fill(10, 50, 69)
    rect(x - (w/2), y-(w/2), w, w)

def drawSquare(n, x, y, sz):
    if n == 5:
        return
    parent_width = sz
    curr = k * parent_width
    s = (width / 2) - mouseX
    if n != 0:
        s = s * (k ** n)
    t = (parent_width / 2) + (curr / 2)
    center_square(x, y, sz)
    
    drawSquare(n+1, x + s, y + t, curr)    #left 
    drawSquare(n+1, x - s, y - t, curr)    # right
    drawSquare(n+1, x + t, y - s, curr)    # top
    drawSquare(n+1, x - t, y + s, curr)    # bottom
     


    
def draw():
    background(255,255,255)

    global k 
    k = float (width - mouseY)/width
    ellipse(mouseX, mouseY, 5, 5)
    noStroke()
    print(mouseY)
    print(mouseX)
    drawSquare(0, 300, 300, 200)
