import random

# defines an individual in the population
class Individual:
        def __init__(self, currentValue):
                self.val = currentValue
                self.fit = 0
                
        
# initializes the population. We assume that we know that each member of the population
# is greater than 0 and less than the input number.
def createGenesis(n):
	return [Individual(random.uniform(0,n)) for i in xrange(0,2*n)]

def getBestCandidates(n, population):
	return sorted(population, key=lambda individual: individual.fit)[:n-1]
	# worstElement = None


	# for newElement in population:
	# 	if len(arr) != 0:
	# 		if len(arr) < n:
	# 			arr.append(newElement)
	# 		else:
	# 			if newElement.fit > worstElement.fit:
	# 				arr.remove(worstElement)
	# 	else:
	# 		arr.append(newElement)
	# 		worstElement = newElement

def morphPopulation(population):
	pass

# calculates the square root of a number using an evolutionary algorithm
def evolutionarySquareRoot(n):
	population = createGenesis(int(n))
	for each in population:
		each.fit = abs(each.val - float(n / each.val))
		print each.val, each.fit
	print "done with original"

	# newPopulationSize
	bestCandidates = getBestCandidates(n, population)
	# print "best candidates"
	# print bestCandidates
	return bestCandidates


#testing
x = evolutionarySquareRoot(10)
for i in x:
        print i.val, i.fit
