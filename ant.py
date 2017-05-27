from aco import distance, tau
import random
import math


class ants:

    def __init__(self, alpha, beta, q_const, evaporation_rate):
        self.not_visited = range(0, 38)
        self.distance_travelled = 0
        self.route = []
        self.evaporation_rate = evaporation_rate
        self.q_const = q_const
        self.alpha = alpha
        self.beta = beta

    def getNextTown(self, current):
        nexttown = [[] for i in range(38)]
        for town in range(0, 38):
            if (town not in self.not_visited):
                print 'continued'
                continue
            nexttown[town] = (
                math.pow(tau[current][town], self.alpha) +
                math.pow(distance[current][town], self.beta)
            )

        # Normalisation
        nexttown = [float(prob) / sum(nexttown) for prob in nexttown]
        # print nexttown

        # Mapping ranks... lowest is highest ranked.
        probz = {}
        while True:
	        for i in range(1, 39):
	        	a = nexttown.index(min(nexttown))
	        	if(a is in self.not_visited):
	        		if(random.random > 0.5):
	        			print "Imma outta da loop"
	        			return a
	        		else:
	        			nexttown.pop(nexttown[a])

        		
       

    def iteration(self):
        nextt = self.getNextTown

    def updateTau(self):
        for i in route - 1:
            tau[i][route[i + 1]] = tau[i][route[i + 1]] + distance_travelled

ant1 = ants(0.8, 0.8, 1, 0.6)
ant1.ranking(1)
