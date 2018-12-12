import numpy
import math

def fitness(distances , individual):
    """
    Returns the total distance between all cities for a given individual
    args:
        distances: numpy array
                   precomputed distances between cities
        individual: list
                indexes of cities
	"""
    total_distance = 0
    distances = numpy.asarray(distances)
    
    for i in range(len(individual)):
        if(i+1 == len(individual)):
            total_distance += distances[individual[i]-1, individual[0] - 1]
        else:
            total_distance += distances[individual[i] - 1, individual[i+1] - 1]

    return total_distance

def distances(cities):
    """
        Returns a 2D matrix of precomputed distances where each 
        row is represented by the city.
        args:
            cities: numpy array
                    vector of coordinates of a city
    """
    distances = numpy.zeros((cities.shape[0],cities.shape[0]))
    for i in range(len(distances)):
        for j in range(len(distances)):
            distances[i,j] = math.sqrt((cities[i,0] - cities[j,0])**2 + (cities[i,1] - cities[j,1])**2)

    return distances

def distance(point1,point2):
    """
        Returns the Euclidean distance between two points 
        args:
            point1: numpy array
                    x,y coordinate
            point2: numpy array 
                    x,y coordinate
    """
    diffx = point2[0]- point2[0]
    diffy = point2[1] - point1[0]

    distance = math.sqrt(diffx**2 + diffy**2)

    return distance

def k_mean(cluster):
        """
	Returns the average of a cluster
	args:
		cluster : numpy array
			  cluster of city coordinates
	"""
        sum_x = 0
        sum_y = 0
        for i in range(cluster.shape[0]):
                sum_x += cluster[i,0]
                sum_y += cluster[i,1]
        average = numpy.array([sum_x/cluster.shape[0],sum_y/cluster.shape[0]])

        return average

        
