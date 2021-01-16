import math as m

# Inputs x and y coords of 2 nodes and outputs distance between them.
def distance(x1,y1,x2,y2):
    delta_x = x2-x1
    delta_y = y2-y1
    return m.sqrt(delta_x**2+delta_y**2)
    
print(distance(0,0,3,4))