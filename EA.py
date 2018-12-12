# COMP3201 - An evolutionary algorithim for the Travelling Salesman Problem
# by Afrah Abdulmajid, Gillian Mensah and Sylvia Unimna

import random
import numpy
from datetime import datetime

from Initialization import *
from Clusters import *
from Calculations import *
from recombination import *
from city import *
from twoOptimal import *
import mutation
import parentSelection
import survivor_selection
import make_bar

def main():
    startTime1 = datetime.now() #to get the time elapsed
    gen_limit = 10000
    
    f = "TSP_WesternSahara_29.txt"
#    f = "TSP_Uruguay_734.txt"
#    f = "TSP_Canada_4663.txt"

    tournament_size = 50
    mut_rate = 0.2
    xover_rate = 0.7

    pop_size = 1000

    mating_pool_size = int(pop_size*0.5) #has to be divisible by 2 
    no_change = int(pop_size *0.25)
    chrom_length = 29
#    chrom_length = 734
#    chrom_length = 4663

    change = False
    gen_ = []
    best_fit = [] #to store the best fitness using tournament for parent selection
    gen = 0
    cities = readFile(f, chrom_length)
    dists = distances(cities)

    population = []
    #population = setCities(pop_size, chrom_length)
    points = Cluster(chrom_length, cities, 4)
    #new_points = two_Opt(points,dists)
    for i in range(pop_size):
        population.append(points)
        
    fitness1 = []
    for ind in range(pop_size):
        fitness1.append(fitness(dists, population[ind]))

    print("Starting Fitness: ", min(fitness1))
    gen_.append(gen)
    best_fit.append(min(fitness1))
    last_min = min(fitness1)
    same_fit = 0

    while gen < gen_limit:
        parents_index = parentSelection.tournament(fitness1, mating_pool_size, tournament_size)
        random.shuffle(parents_index)
        offspring = []
        offspring_fitness = []
        i = 0
        while len(offspring) < mating_pool_size:
            startTime2 = datetime.now()
            if random.random() < xover_rate:
                off1, off2 = order_crossover(population[parents_index[i]], population[parents_index[i+1]])
##                if change:
##                    off1, off2 = m_order(population[parents_index[i]], population[parents_index[i+1]], dists)
##                else:
##                    off1, off2 = greedyCrossover(population[parents_index[i]], population[parents_index[i+1]])
##                    #off1, off2 = order_crossover(population[parents_index[i]], population[parents_index[i+1]])
               
            else:
                off1 = population[parents_index[i]].copy()
                off2 = population[parents_index[i+1]].copy()
            
                
            if random.random() < mut_rate:
                if change:
                    off1 = mutation.inversion_mutation(off1)
                else:
                    off1 = mutation.swap_mutate(off1)
            if random.random() < mut_rate:
                if change:
                    off2 = mutation.inversion_mutation(off2)
                else:
                    off2 = mutation.swap_mutate(off2)
                    
            offspring.append(off1)
            offspring_fitness.append(fitness(dists, off1))
            offspring.append(off2)
            offspring_fitness.append(fitness(dists, off2))
            i += 2
            
        population, fitness1 = survivor_selection.mu_plus_lambda(population, fitness1, offspring, offspring_fitness)
        gen += 1
        gen_.append(gen)
        minim = min(fitness1)
        #print(gen, minim)
        indi = fitness1.index(min(fitness1))
        best_fit.append(min(fitness1))
        individual = population[indi]
        my_time = 0
        if minim == last_min:
            same_fit += 1
        else:
            last_min = min(fitness1)
            same_fit = 0
        if change == True and same_fit == no_change:
            print("Stopped at Generation: ", gen)
            break
        if same_fit == no_change:
            change = True
            same_fit = 0
            print("Changed to inversion Mutation at Generation: ", gen)
        #print('\n Time Elapsed in General: ', datetime.now() - startTime1)        
            
    print("Ending Fitness: " ,minim)
    print('\n Time Elapsed in General: ', datetime.now() - startTime1)
    mycity = city_xy(individual, cities)
    make_bar.make_Bar(gen_, best_fit)

    make_bar.make_Plot(mycity)
##

main()       
##
##        
