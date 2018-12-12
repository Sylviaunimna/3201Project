import random
from random import randrange
import numpy

def swap_mutate(individual):
    """
        Performs swap mutation on an individual
        args:
            individual: list
                    indexes of cities
    """
    mut = individual.copy()
    mut_points = random.sample(range(len(individual)),2)
    temp = individual[mut_points[0]]
    mut[mut_points[0]] = mut[mut_points[1]]
    mut[mut_points[1]] = temp
    return mut

def inversion_mutation(individual):
    """
        Performs inversion mutation on an individual
        args:
            individual: list
                    indexes of cities
    """
    mut = individual.copy()
    index1 = randrange(0,len(individual))
    index2 = randrange(index1,len(individual))
    pop_mid = int((index2 - index1)/2)
    j = 0
    while (j <= pop_mid):
        temp = mut[index1]  
        mut[index1] = mut[index2]
        mut[index2] = temp
        index1 += 1
        index2 -= 1
        j += 1
    return mut

