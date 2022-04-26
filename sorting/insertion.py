import pyglet

# Persistent variables
arr = None
i, iteration = 1, 0
previously_selected = None


# Set variables in readiness for iteration
def init(array: list):
    global arr, i, iteration, previously_selected
    arr = array
    i, iteration = 1, 0
    previously_selected = None


# Iteration that would normally be found inside a while/for loop
def iterate(dt):
    global arr, i, iteration, previously_selected

    if previously_selected:
        previously_selected.unhighlight()

    # End case
    if iteration >= len(arr)-1:
        pyglet.clock.unschedule(iterate)
        print("Finished")
        return
    
    # End of an iteration
    if i == 0:
        iteration += 1
        i = iteration + 1
        return
    
    # Highlight current array item on screen
    arr[i].highlight()
    previously_selected = arr[i]

    # If item is in the correct place
    if arr[i-1].value < arr[i].value:
        iteration += 1
        i = iteration + 1
        return
        
    # Else swap items
    else:
        temp = arr[i]
        arr[i] = arr[i-1]
        arr[i-1] = temp
        arr[i].set_index(i)
        arr[i-1].set_index(i-1)
    
    i-=1
