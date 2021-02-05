#!/usr/bin/python
#-----------------------------------------------------------------------------------------------------------------------------------------
# Author: Sarah Spence & Copyright: HackerRank
# Date: 2021-02-01
# Title: Bot Saves Princess Challenge
# Description: This takes an input value n denoting the size of an n by n grid. The script then takes input for a grid where, p
#              represents princess peach in one of the four corners of the grid, and m denotes the player starting in the center
#              of the grid. The sample input below shows n = 3 and princess peach in the top right corner. The script returns the
#              quickest path to the princess. 
#              Sample input: line 1: 3
#                            line 2: --p
#                            line 3: -m-
#                            line 4: ---
#---------------------------------------------------------------------------------------------------------------------------------------
import sys

# Function to find princess peach in the fewest steps
def displayPathtoPrincess(m,grid):
    # Calculate number of steps
    steps = int((m-1)/2)
    
    # Print moves
    if grid[0][0] == 'p':
        for i in range(steps):
            print("UP")
            print("LEFT")
    elif grid[m-1][0] == 'p':
        for i in range(steps):
            print("DOWN")
            print("LEFT")
    elif grid[0][m-1] == 'p':
        for i in range(steps):
            print("UP")
            print("RIGHT")
    elif grid[m-1][m-1] == 'p':
        for i in range(steps):
            print("DOWN")
            print("RIGHT")

def main(): 
    # Hacker Rank's code below      
    m = int(input())
    grid = [] 
    for i in range(0, m): 
        grid.append(input().strip())

    displayPathtoPrincess(m,grid)
if __name__ == "__main__":
    sys.exit(main())
