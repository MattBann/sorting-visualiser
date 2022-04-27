import pyglet

# Persistent variables
arr = None
i, iteration = 0, 0
previously_selected = None
running = True

# Set variables in readiness for iteration
def init(array: list):
    global arr, i, iteration, previously_selected, running
    arr = array
    i, iteration = 0, 0
    previously_selected = None
    running = True


# Iteration that would normally be found inside a while/for loop
def iterate(dt):
    global arr, i, iteration, previously_selected, running

    if previously_selected:
        previously_selected.unhighlight()

    # End case
    if iteration >= len(arr):
        pyglet.clock.unschedule(iterate)
        print("Finished")
        running = False
        return
    
    # End of an iteration
    if i == len(arr) - iteration - 1:
        i = 0
        iteration += 1
        return
    
    # Highlight current array item on screen
    arr[i].highlight()
    previously_selected = arr[i]

    # If items need to be swapped to be in order, swap them
    if arr[i].value > arr[i+1].value:
        temp = arr[i]
        arr[i] = arr[i+1]
        arr[i+1] = temp
        arr[i].set_index(i)
        arr[i+1].set_index(i+1)
    
    i+=1
