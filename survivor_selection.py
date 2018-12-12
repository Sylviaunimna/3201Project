def mu_plus_lambda(current_pop, current_fitness, offspring, offspring_fitness):
    """
        Use mu plus lambda selection to select population number of individuals
        as survivors.
        args:
            current_pop: list
                        population of a group on individuals
            current_fitness: list
                            fitness of the group of individuals in the population
            offspring: list
                       population of a group on individuals
            offspring_fitness: list
                               fitness of the group of individuals in the offspring 
    """
    population = []
    fitness = []
    temp_pop = current_pop + offspring
    temp_fitness = current_fitness + offspring_fitness
    temp_fitness,temp_pop = zip(*sorted(zip(temp_fitness, temp_pop),reverse = False))
    for j in range(0,len(current_pop)):
        population.append(temp_pop[j])
        fitness.append(temp_fitness[j])
    
    return population, fitness
