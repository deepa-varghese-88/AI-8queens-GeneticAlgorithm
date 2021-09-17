import random
import matplotlib.pyplot as plt


#NOTE: As of now the code only works for 8 queens. the value 8 has been hardcoded in several places.
#To increase the number of queens, replace the hardcoded values with a single variable which can be initialised under 
#-------- MAIN -------#
#
#How to run the code:
#
#1) Open the code in a python editor
#2) Under the comment #-------- MAIN -------#, you'll find the variables that govern the program run
#3) To modify Mutation probability, change value of MutationPct to any value between (0.0 - 1.0)
#4) To modify the population size, change value of PopulationSize
#5) To modify the number of iterations for which a the code can run till it can give, change value of NumIterations

class Individual:
    def __init__(self, indiv):
        self.indiv = indiv
        self.fitness = self.fitnessfunction()
        self.si = 2         #any nonsensical number

    def fitnessfunction(self) -> int:
        nonattacking = 0
        for i in range(len(self.indiv)):
            h = i - 1
            j = i + 1
            right = left = 1
            while (h >= 0 or j < len(self.indiv)):
                if h>= 0 :
                    if self.indiv[h] != self.indiv[i] and self.indiv[h] != self.indiv[i]-left and self.indiv[h] != self.indiv[i]+left :
                        nonattacking += 1
                    left += 1
                    h -= 1
                if j < len(self.indiv):
                    if self.indiv[j] != self.indiv[i] and self.indiv[j] != self.indiv[i]-right and self.indiv[j] != self.indiv[i]+right :
                        nonattacking += 1
                    right += 1
                    j += 1
        nonattacking = nonattacking/2
        return nonattacking

    # def display(self):
    #     disp = []
    #     i = 0
    #     #for queen in self.indiv:

def roulette(population):
    x = random.random()
    current = 0
    for individual in population:
        current += individual.si
        if current > x:
            return individual

def newPopulation(population):
    newPopulation = []
    while len(newPopulation) < PopulationSize:
        parent1 = roulette(population).indiv
        parent2 = roulette(population).indiv
        crossover = random.randint(0, 7)
        child1 = parent1[:crossover] + parent2[crossover:]
        child2 = parent2[:crossover] + parent1[crossover:]
        mutation(child1)
        mutation(child2)
        newPopulation.append(Individual(child1))
        newPopulation.append(Individual(child2))
    sumfitness = sum(c.fitness for c in newPopulation)
    for individual in newPopulation:
        individual.si = individual.fitness / sumfitness
    avgfitness = sumfitness/PopulationSize
    return (newPopulation, avgfitness)

def mutation(child):
    if(random.random() < MutationPct):
        index = random.randint(0,7)
        child[index] = random.randint(1,8)

def myplot(numofgenerations, avgfitnessarray):
    plt.plot(numofgenerations, avgfitnessarray)
    plt.ylabel("Average fitness")
    plt.xlabel("Generation")
    #plt.yticks(range(0,30,2))
    #plt.xticks(range(0,100,10))
    plt.ylim(0,28)
    plt.tight_layout()
    plt.show()

#-------- MAIN -------#

MutationPct = 0.3
PopulationSize = 100
NumIterations = 500
population = []

for i in range(PopulationSize):
   population.append(Individual(random.sample(range(1,9),8)))
sumfitness = sum(c.fitness for c in population)
for individual in population:
    individual.si = individual.fitness / sumfitness
avgfitness = sumfitness/PopulationSize
print("Initial population")
for individual in population:
    print(individual.indiv, '  ', individual.fitness, '  ', individual.si)

count = 0
numofgenerations = [0]
avgfitnessarray = [avgfitness]
while count < NumIterations:
    count += 1
    numofgenerations.append(count)
    print("Iteration: ", count)
    (population, avgfitness) = newPopulation(population)
    avgfitnessarray.append(avgfitness)
    # print(avgfitness)
    # for individual in population:
    #        print(individual.indiv, '  ', individual.fitness, '  ', individual.si)
    for individual in population:
        if individual.fitness == 28:
            for elem in population:
                   print(elem.indiv)
            print("Resolved: ", individual.indiv)
            myplot(numofgenerations, avgfitnessarray)
            exit(1)

print(count, " Iterations completed")

