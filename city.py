import numpy
from datetime import datetime


population = numpy.array([])

def readFile(filename, chromLength): 
    """
    Reads a file in and returns a numpy array 
    of each line of the file(x,y) 
    args:
        filename: .txt file 
                  file of coordinates
        chromLength: int
                     number of cities   
    """
    population = numpy.zeros((chromLength, 2))
    lines = open(filename, 'r')
    myline = lines.read().splitlines()
    i = 0
    for x in myline:
        population[i] = numpy.array([x.split(' ')[1], x.split(' ')[2]])
        i +=1
        
    
    lines.close()
    return population

def city_xy(indexes, coords):
    """
    Returns a numpy array of x,y coordinates of specified 
    city indexes
    args:
        indexes: list
                  indexes of cities
        coords: numpy arrau
                numpy aray of all cities in the population  
    """
    cities = numpy.zeros((len(indexes), 2))
    for i in range(len(indexes)):
        cities[i] = coords[indexes[i]-1]
    return cities


        
    
    


    




