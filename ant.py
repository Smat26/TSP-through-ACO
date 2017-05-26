from aco import distance,tau
import random
import math
class ants:


	def __init__(self, alpha, beta, q_const, evaporation_rate):
		self.not_visited = range(0,38)
		self.distance_travelled = 0
		self.route = []
		self.evaporation_rate = evaporation_rate
		self.q_const =  q_const
		self.alpha = alpha
		self.beta = beta

	def ranking(self,current):
		nexttown = [[] for i in range(38)]
		for town in range(0,38):
			if (town not in self.not_visited):
				print 'continued'
				continue
			nexttown[town] =(
				math.pow(tau[current][town],self.alpha) + math.pow(distance[current][town],self.beta)
				)

		# Normalisation
		nexttown = [float(prob)/sum(nexttown) for prob in nexttown]
		# print nexttown

		#Mapping ranks... lowest is highest ranked.
		probz = {}
		for i in range(1,39):
			probz[i] = nexttown[i-1];
		print probz	

	def iteration(self):
		return 0

	def updateTau(self):
		for i in route-1:
			tau[i][route[i+1]] = tau[i][route[i+1]] + distance_travelled

ant1 = ants(0.8,0.8,1,0.6)
ant1.ranking(1)