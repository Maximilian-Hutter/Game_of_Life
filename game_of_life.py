from time import sleep
import numpy as np
from numpy.random import default_rng
from random import randrange
from custom_functions import *
from graphics import debugout
SIZE = 10

grid = np.zeros((SIZE,SIZE),dtype=bool)

grid = generate_input(grid,SIZE)

while True:
    debugout(grid)
    grid = advance_iteration(grid,SIZE)

    if randrange(0,10) == 5 :   # 1 in 100 chance to add an additional pattern to input
        grid = generate_input(grid,SIZE)
    if grid.sum() == 0:
        grid = generate_input(grid,SIZE)

