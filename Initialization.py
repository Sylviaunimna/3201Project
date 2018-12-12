from numpy.random import permutation
def setCities(pop_size,chromlength):
        """
        Returns a list of permuatations of size population.
        args:
            pop_size: int
                      number of permuations to be returned
            chromLength: int
                         number of cities
        """      
        newpop = []   
        for i in range (pop_size):
        	newpop.append(permutation([i for i in range(1, chromlength + 1)]).tolist())
        return newpop

       



