import math
import numpy as np
import random
import city
from Calculations import *

def Cluster(chromLength, coords, clusters):

    """
        Groups the cities into clusters and returns a list of them combined
        args:
            chromLength: int 
                         number of cities 
            coords: numpy array 
                    city coordinates
            clusters: int
                      number of clusters(k)
    """
    index = random.sample(range(chromLength),clusters)
    cluster_array = [[], [], [], []]
    centroids = []
    for i in range(clusters):
        cluster_array[i].append(index[i]+1) #to put the initial clusters in
        centroids.append(coords[index[i]]) #append the mean, the mean of one element is just the element 

    for i in range(chromLength):
        if i not in index:
            mindist = math.inf
            for j in range(clusters): #to get the mean with the least distance to the coordinate
                dist = distance(centroids[j], coords[i])
                if mindist > dist:
                    mindist = dist
                    lowest = j
            cluster_array[lowest].append(i+1)
            for x in range(clusters):
                cluster = city.city_xy(cluster_array[x], coords) #gets the coordinates corresponding to the index
                centroids[x] = k_mean(cluster)
    final_c = []
    for i in range(clusters):
        final_c += cluster_array[i]
    return final_c

        


    




