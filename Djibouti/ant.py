from aco import distance, tau, towns
import random
import math
from pprint import pprint
import matplotlib.pyplot as plt
from operator import add


class ants:

    def __init__(self, alpha, beta, q_const, evaporation_rate):
        self.not_visited = range(0, towns)
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
        nexttown = [[] for i in range(towns)]
        for town in range(0, towns):

            if (town not in self.not_visited or town == current):
                nexttown[town] = -1
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
            a = nexttown.index(max(nexttown))
            # print "Candidates: "+ str(nexttown)
            # print "minimum: "+ str(a)

            if(random.random > 0.3):
                # print "Imma outta da loop"
                # print 'next town:'
                # print a
                return a
            else:
                nexttown.pop(nexttown[a])

    def iteration(self):
        self.distance_travelled = 0
        self.route = []
        while(self.not_visited):
            nextt = self.getNextTown(self.current)
            # print self.route
            self.distance_travelled = self.distance_travelled + \
                distance[self.current][nextt]
            # print self.distance_travelled
            self.route.append(nextt)
            # print "Not visited: "+ str(self.not_visited)
            # print "Nextt: "+ str(nextt)
            self.not_visited.pop(self.not_visited.index(nextt))
            self.current = nextt

        if(not self.not_visited):
            self.tourEnded()

    def tourEnded(self):
        # print "Route: " + str(self.route)
        self.updateTau()
        self.not_visited = range(0, towns)
        self.tours = self.tours + 1
        self.distance_travelled = self.distance_travelled + distance[self.route[0]][self.route[-1]]
        self.cum_distance_travelled = self.cum_distance_travelled + self.distance_travelled
        self.current = random.randint(0,towns-1)
        # print self.distance_travelled

    def updateTau(self):
        for i in range(0, len(self.route) - 1):
            tau[self.route[i]][self.route[i + 1]] = (float(
                tau[self.route[i]][self.route[i + 1]]) * self.evaporation_rate) + (self.q_const / self.distance_travelled)
            tau[self.route[i + 1]][self.route[i]] = (float(
                tau[self.route[i + 1]][self.route[i]]) * self.evaporation_rate) + (self.q_const / self.distance_travelled)

        # print tau
    def Initialize(self):
        rand = random.randint(0, towns-1)
        # print rand
        self.current = rand
        self.not_visited.pop(self.not_visited.index(rand))
        self.route.append(rand)

# Paramters for ACO:
no_of_ants = 10
evaporation_rate =0.6
q_const = 1
alpha = 0.8
beta = 0.8

colony = [ants(alpha, beta, q_const, evaporation_rate)
          for i in range(0, no_of_ants)]
tours = 100

for ant in colony:
    ant.Initialize()

r_dist_avg = [0 for i in range(0,tours)]
r_dist_best = [[] for i in range(0,tours)]
r_dist_temp = []

r_tour_dist_avg = [0 for i in range(0, tours)]
r_tour_dist_best = [0 for i in range(0, tours)]
r_tour_dist_temp = []

# 10 runs to smoothen things out
for k in range(0, 10):
    # Looping for each tour
    for i in range(0, tours):
        # Iteration for each ant
        for ant in colony:
            ant.iteration()
            r_dist_avg[i] = r_dist_avg[i] + ant.distance_travelled
            r_dist_temp.append(ant.distance_travelled)

        r_dist_avg[i] = r_dist_avg[i] / no_of_ants
        r_dist_best[i] = min(r_dist_temp)
        print 'Tour no: ' + str(i + 1)
        print 'Route: ' + str(colony[r_dist_temp.index(min(r_dist_temp))].route)
        print 'Distance: ' + str(colony[r_dist_temp.index(min(r_dist_temp))].distance_travelled)
        print "----------------------------------------------------------------------------------------------"
        r_dist_temp = []
    r_tour_dist_avg = map(add,r_tour_dist_avg,r_dist_avg)
    r_tour_dist_best = map(max, r_tour_dist_best, r_dist_best)

r_tour_dist_avg = [dist/10 for dist in r_tour_dist_avg]

plt.plot(range(0, tours), r_tour_dist_avg, 'r-', label='Average Distance')
plt.plot(range(0, tours), r_tour_dist_best, 'b-', label='Best Distance')
# pprint(tau)
# Now add the legend with some customizations.
legend = plt.legend(loc='upper center', shadow=True)

plt.xlabel('Tours')
plt.ylabel('Distance')
plt.title('Distance on each tour')
plt.show()