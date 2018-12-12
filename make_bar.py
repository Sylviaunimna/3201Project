import matplotlib.pyplot as plt
import numpy

def make_Bar(gen, fitness):
    """
    Plots a graphical representation of the change in fitness as the
    generation increases    
    args:
        gen: list
              list of generations
        fitness: list
                 corresponding best fitnesses for each generation
    """
    plt.plot(gen,fitness, color = 'black', label = 'Tournament')

    plt.xlabel("Generation")
    plt.ylabel("Fitness")
    plt.title("Best fitness of all generations")
    plt.legend()
    plt.show()

def make_Plot(population):
    """
    Plots a graphical representation of  the route the best individual took across the points.
    args:
        population: numpy array
                    coordinates of best individual
    """
    individual = population.tolist()
    plt.xlabel("Longitude")
    plt.ylabel("Latitude")
    xcord = []
    ycord = []
    for i in range(len(individual)):
        xcord.append(individual[i][0])
        ycord.append(-individual[i][1])
    xcord.append(individual[0][0])
    ycord.append(-individual[0][1])
    plt.plot(ycord, xcord, c = "k", marker = "o", markersize = 5, label = "Cities")
    plt.show()



