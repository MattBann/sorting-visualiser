from typing import Callable
import pyglet
import visuals
import sorting.bubble as bubble
import sorting.insertion as insertion

# Use foreground and background batch graphics processors to avoid layer issues
controller_batch_background = pyglet.graphics.Batch()
controller_batch_foreground = pyglet.graphics.Batch()

arr = None

# Length of array to be sorted
size = 50

# Label definitions
size_label = pyglet.text.Label(text=str(size), x=160, y=180, batch=controller_batch_foreground)

def update_labels():
    size_label.text = str(size)

# Class defining a button. Uses a rectangle for the shape and a label for the text
class Button:

    # Constructor. Takes position, size, text and a callable (function) used when clicked
    def __init__(self, x:int, y:int, width:int, height:int, text:str="", button_action:Callable=None) -> None:
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        self.action = button_action
        self.text = pyglet.text.Label(
            text, font_name="Arial", 
            batch=controller_batch_foreground, 
            anchor_x='center', anchor_y='center', 
            x=(x+width//2), y=(y+height//2), 
            color=(0,0,0,255),
            width=width,
            multiline=True
            )
        self.button_box = pyglet.shapes.Rectangle(x, y, width, height, color=(112, 213, 229), batch=controller_batch_background)
    

    def press_button(self):
        try:
            self.action()
        except:
            return -1


# Incremental setters for array length with validation to keep within a range
def increase_size():
    global size
    if size < 100 : size+=1
    update_labels()
def decrease_size():
    global size
    if size > 4 : size-=1
    update_labels()


# Create hidden window which will show the array being sorted
visuals_window = pyglet.window.Window(caption="Visualiser", visible=False, resizable=True)


# Draw the visualisation window. Clear the screen then draw the bars
@visuals_window.event
def on_draw():
    visuals_window.clear()
    visuals.visuals_batch.draw()


# Create the array and show the visualisation window
def show_visuals():
    if visuals_window.visible:
        return
    global arr
    arr = visuals.create_array(size)
    visuals_window.set_size(size*20, size*10)
    visuals_window.set_visible(True)


# Close the visualisation window. Also called on control_window.on_close() in main. Exits the program
@visuals_window.event
def on_close():
    pyglet.app.exit()


# Run an algorithm. Pyglet clock controls iteration
def run_bubble():
    bubble.init(arr)
    pyglet.clock.schedule_interval(bubble.iterate, 1/60)

def run_insertion():
    insertion.init(arr)
    pyglet.clock.schedule_interval(insertion.iterate, 1.60)


# Create and return a list of elements that a drawn inside the control window, including buttons and labels
def create_control_window():
    elements = []
    elements.append(size_label)
    elements.append(pyglet.text.Label("No. items", x=70, y=180, batch=controller_batch_foreground))
    elements.append(Button(200, 180, 40, 17, "Up", increase_size))
    elements.append(Button(250, 180, 40, 17, "Down", decrease_size))
    elements.append(Button(160, 140, 80, 20, "Show", show_visuals))
    elements.append(Button(160, 80, 80, 20, "Bubble", run_bubble))
    elements.append(Button(160, 50, 80, 20, "Insertion", run_insertion))
    return elements