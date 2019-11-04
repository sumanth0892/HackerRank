#The test cases worked on my personal IDE but not on the HackerRank interface. 
import os
import numpy as np
def gridLand(n,m,k,track):
    grid = np.zeros((n,m))
    for t in track:
        r,c1,c2 = t
        r -= 1
        c1 -= 1
        c2 -= 1
        grid[r,c1:c2+1] = 1
    return np.count_nonzero(grid == 0)



    
