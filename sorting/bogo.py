import random
import pyglet

# Persistent variables
arr = None
running = False

# Set variables in readiness for iteration
def init(array: list):
    global arr, previously_selected, running
    arr = array
    previously_selected = None
    running = True

# Determine whether the data is sorted
def is_sorted(data) -> bool:
    return all(a.value <= b.value for a, b in zip(data, data[1:]))


# Iteration that would normally be found inside a while/for loop
def iterate(dt):
    global arr, running
    
    # End case
    if is_sorted(arr):
        pyglet.clock.unschedule(iterate)
        print("Finished")
        running = False
        return
    
    # Randomise order of array and hope its sorted
    random.shuffle(arr)
    for i in range(len(arr)):
        arr[i].set_index(i)
    
