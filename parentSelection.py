from random import *
import builtins
import math

#tournament selection without replacement
def tournament(fitness, mating_pool_size, tournament_size):
    """
        Returns a list of indexes of selected parents using the
        tournament selection method.An individual wins a tournament
        if they have the shortest path(smallest fitness)
        
        args:
            fitness: list
                     fitnesses of individuals in a population
            mating_pool_size: int
                              number of individuals that need to be selected
            tournament_size: int
                             number of individuals to compete in a tournament 
    	"""
    selected_to_mate = [] # list of the indices of picked parents

    current_member = 1
    size = []
    Min = math.inf
    index = 0
    while (len(selected_to_mate) <mating_pool_size):
        Min = math.inf
        index = 0
        size = sample(range(len(fitness)), tournament_size)
        for i in range(len(size)):
            if fitness[size[i]] < Min:
                Min = fitness[i]
                index = size[i]
        selected_to_mate.append(index)
        current_member += 1
    #student code end
    return selected_to_mate




 


