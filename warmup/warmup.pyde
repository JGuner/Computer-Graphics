width = 600
center = width/2.0
def setup():
    size(width, width)
def center_square(x,y,w):
    rect(x - (w/2), y-(w/2), w, w)
    

def draw():
    background(255,255,255)
    s = (mouseX)
    t = (width/3) - (.5*(width-mouseY)*(.33))
    neg_s = (width - mouseX)
    center_square(300, 300, 200)
    for i in range(5):
        k = (.5) ** i
        
        fill(0,0,0)
    #top
        center_square(s, (k*t), k*(width-mouseY)*(.33))
    #left
        center_square(k*t, neg_s , k*(width-mouseY)*(.33))
    #bottom
        center_square(neg_s, width-k*t , k*(width-mouseY)*(.33))
    #right
        center_square(width-k*t, s, k*(width-mouseY)*(.33))
        fill(255,0,0)
    ellipse(mouseX, mouseY, 5, 5)
    print(mouseY)
    print(mouseX)


    
