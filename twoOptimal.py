from Calculations import *  
def two_Opt(individual,distMatrix):
    best = individual
    improved = True
    while(improved):
        improved = False
        for i in range(1,len(individual)-2):
            for j in range(i+1, len(individual)):
                if ((j-i) == 1):
                    continue
                new_route = individual[:]
                new_route[i:j] = individual[j-1:i-1:-1]
                if(fitness(distMatrix,new_route) < fitness(distMatrix,best)):
                   best = new_route
                   improved = True
        individual = best
    return best
        
           

        

        
