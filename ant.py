from aco import distance, tau
import random
import math
from pprint import pprint

class ants:

    def __init__(self, alpha, beta, q_const, evaporation_rate):
        self.not_visited = range(0, 38)
        self.distance_travelled = 0
        self.cum_distance_travelled = 0
        self.route = []
        self.evaporation_rate = evaporation_rate
        self.q_const = q_const
        self.alpha = alpha
        self.beta = beta
        self.tours = 0
        self.current = 100

    def getNextTown(self, current):
        nexttown = [[] for i in range(38)]
        for town in range(0, 38):

            if (town not in self.not_visited or town == current):
                nexttown[town] = float('inf')
                continue
            nexttown[town] = (
                math.pow(tau[current][town], self.alpha) +
                math.pow(1 / distance[current][town], self.beta)
            )
            # print nexttown

        # Normalisation
        # nexttown = [float(prob) / sum(nexttown) for prob in nexttown]
        # print nexttown

        # Mapping ranks... lowest is highest ranked.
        while True:
            a = nexttown.index(min(nexttown))
            # print "Candidates: "+ str(nexttown)
            # print "minimum: "+ str(a)
            if(a in self.not_visited):
                if(random.random > 0.5):
                    # print "Imma outta da loop"
                    return a
                else:
                    nexttown.pop(nexttown[a])

    def iteration(self):
        while(self.not_visited):
            nextt = self.getNextTown(self.current)
            self.distance_travelled = self.distance_travelled + \
                distance[self.current][nextt]
            # print self.distance_travelled
            self.route.append(nextt)
            # print "Not visited: "+ str(self.not_visited)
            # print "Nextt: "+ str(nextt)
            self.not_visited.pop(self.not_visited.index(nextt))
            self.current = nextt

        if(not self.not_visited):
            # print "Tour Completed"
            print "Route: " + str(self.route)
            self.updateTau()
            self.route = []
            self.not_visited = range(0, 38)
            self.tours = self.tours + 1
            self.cum_distance_travelled = self.cum_distance_travelled + self.distance_travelled
            print self.distance_travelled
            self.distance_travelled = 0

    def updateTau(self):
        for i in range(0, len(self.route) - 1):
            tau[self.route[i]][self.route[i + 1]] = float(
                tau[self.route[i]][self.route[i + 1]]) + (self.q_const / self.distance_travelled)
            tau[self.route[i + 1]][self.route[i]] = float(
                tau[self.route[i + 1]][self.route[i]]) + (self.q_const / self.distance_travelled)

        # print tau
    def Initialize(self):
        rand = random.randint(0, 37)
        # print rand
        self.current = rand
        self.not_visited.pop(self.not_visited.index(rand))
        self.route.append(rand)

# Paramters for ACO:
no_of_ants = 50
evaporation_rate = 0.6
q_const = 1
alpha = 0.8
beta = 0.8

colony = [ants(alpha, beta, q_const, evaporation_rate) for i in range(0, no_of_ants)]
tours = 500

for ant in colony:
    ant.Initialize()

for i in range(0, tours):
    for ant in colony:
        ant.iteration()


