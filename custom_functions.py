import numpy as np
from numpy.random import default_rng
from random import randrange

def padding(array, xx, yy):
    """
    :param array: numpy array
    :param xx: desired height
    :param yy: desirex width
    :return: padded array
    """

    h = array.shape[0]
    w = array.shape[1]

    a = (xx - h) // 2
    aa = xx - a - h

    b = (yy - w) // 2
    bb = yy - b - w

    return np.pad(array, pad_width=((a, aa), (b, bb)), mode='constant')


def create_pattern(SIZE):  # create a pattern as input because random placements probably die quickly
    rng = default_rng()
    pattern = rng.choice(2, (randrange(2,10),randrange(2,10)))
    pattern = padding(pattern, SIZE,SIZE)
    return pattern

def generate_input(grid,SIZE):   # generate input at the start of the game

    pattern = create_pattern(SIZE)
    input_grid = np.logical_or(grid, pattern)

    return input_grid

def get_neighbors(grid, index):

    num_neighbor = 1
    left = max(0,index[0]-num_neighbor)
    right = max(0,index[0]+num_neighbor+1)

    bottom = max(0,index[1]-num_neighbor)
    top = max(0,index[1]+num_neighbor+1)

    neighbors = grid[left:right,bottom:top]

    return neighbors



def advance_iteration(grid,SIZE):    # check which cells are dead and which are alive and advance the game
    
    # deaths calc

    new_grid = np.ones((SIZE,SIZE))
    indices = np.argwhere(grid==True)

    for i, index in enumerate(indices, start=0):

        neighbors = get_neighbors(grid,index)
        _,count = np.unique(neighbors, return_counts=True)

        try:
            count[1] = count[1] - 1
            if count[1] < 2:
                new_grid[index[0],index[1]] = 0
            if count[1] > 3:
                new_grid[index[0],index[1]] = 0
        except:
            count = [count[0],0]
            if count[1] < 2:
                new_grid[index[0],index[1]] = 0
            if count[1] > 3:
                new_grid[index[0],index[1]] = 0


    # new life
    new_grid = np.zeros((SIZE,SIZE))

    num_neighbor = 1

    for index in indices:
        left = index[0]-num_neighbor
        right = index[0]+num_neighbor

        bottom = index[1]-num_neighbor
        top = index[1]+num_neighbor

        for i in range(left, right):
            for a in range(bottom, top):
                if grid[i,a] == False:
                    index = [i,a]

                    neighbors = get_neighbors(grid,index)
                    _,count = np.unique(neighbors, return_counts=True)
                    count[0] = count[0] - 1
                    try:
                        if count[1] == 3:
                            new_grid[index[0], index[1]] = 1
                    except:
                        count = [count[0], 0]
                        if count[1] == 3:
                            new_grid[index[0], index[1]] = 1


    grid = np.logical_or(grid,new_grid)

    # deaths overwrite

    grid = np.logical_and(grid,new_grid)

    return grid