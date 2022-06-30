from .maze_generation import maze
from .Algorithms import algorithms

def run():
    for alg in algorithms:
        alg.run()