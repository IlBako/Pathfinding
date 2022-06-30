from .maze_generation import maze
from .Algorithms import algorithms

start_pos = maze.find_start()

def setup():    
    for alg in algorithms:
        alg.setup(maze)

def run():
    for alg in algorithms:
        alg.run(start_pos)