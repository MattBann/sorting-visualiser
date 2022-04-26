import random
import pyglet

visuals_batch = pyglet.graphics.Batch()


# Class defining an array item. Adds extra properties to the BorderedRectange class
class ArrItem(pyglet.shapes.BorderedRectangle):

    def __init__(self, index, value) -> None:
        super().__init__(index*20, 0, 20, value*10, batch=visuals_batch)
        self.value = value
        self.index = index
        
        self.highlighted = False

    # Update position on screen to reflect changed index
    def set_index(self, new_index):
        self.index = new_index
        self.x = new_index*20
    
    # Change the colour to indicate currently being moved
    def highlight(self):
        self.color = (48, 221, 198)
    
    def unhighlight(self):
        self.color = (255, 255, 255)


# Create an array of the given size containing a ArrItems in a random order
def create_array(size):
    arr = []
    for i in range(size):
        arr.append(ArrItem(i,i))
    
    random.shuffle(arr)
    for i in range(size):
        arr[i].set_index(i)
    
    return arr