from aco import distance
import random
class ants:
	tau = [[0] for i in range(37)]

	def __init__(self, alpha, beta, q_const, evaporation_rate):
		self.not_visited = range(1,39)
		self.distance_travelled = 0
		self.route = []
		self.evaporation_rate = evaporation_rate
		q_const =  q_const
		self.alpha = alpha
		self.beta = beta

	def iteration(self):
		print self.tau

	def updateTau(self):
		for i in range(0, 37):
		    for j in range(0, 37):
		        tau[i].append(
		            (((y_coord[i] - y_coord[j]) * (y_coord[i] - y_coord[j])) +
		             ((x_coord[i] - x_coord[j]) * (x_coord[i] - x_coord[j])))
		        )
        

ant1 = ants(0.8,0.8,1,0.6)
ant1.iteration()