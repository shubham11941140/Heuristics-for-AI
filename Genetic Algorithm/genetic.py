from random import randint, seed

# function to generate generate_chromosomes of length n
def generate_chromosome(n):
    return [randint(0, 1) for _ in range(n)]

# function to calculate the fitness of the gene
""" we are also taking care of the fact that if two gene have same value but different weights
then the gene with lower weight will have more fitness """
def fitness(gene, weights, value, loss, max_weight, sum_weight):

    total_value = 0
    weight = 0

    for i, item in enumerate(gene):

        if not item:
            total_value -= (loss[i])

        else:
            weight += weights[i]
            total_value += value[i]

    return 0 if (weight > max_weight) | (total_value < 0) else (total_value * sum_weight) + (sum_weight - weight)

# the function defined for choosing the best gene
def choose(fit_values):

    total_value = 0
    prob = []

    for val in fit_values:
        total_value += val
        prob.append(total_value)

    guess = randint(0, total_value - 1)
    prev = 0

    for i, item in enumerate(prob):

        if (guess >= prev) & (guess < item):
            return i

        prev = item

# the function responsible for cross breeding and mutation
def cross_mut(gene_a, gene_b):

    #choosing a random slicing point to cut the gene into two parts
    a = randint(0, len(gene_a) - 1)

    for i in range(a + 1):
        gene_a[i], gene_b[i] = gene_b[i], gene_a[i]

    #the code for mutation start from here
    for i in range(len(gene_a)):

        val = randint(0, 9)

        if not val:
            gene_a[i] = abs(gene_a[i] - 1)

        val2 = randint(0, 9)

        if not val2:
            gene_b[i] = abs(gene_b[i] - 1)

    return [gene_a, gene_b]

# the function used in copying a array into another array
def gen_arr(arr):
    return arr.copy()

# the final fitness function which doesn't consider the weight when calculating fitness
def actual_fitness(gene,value,loss):

    result = 0

    for i, item in enumerate(gene):
        result = result + value[i] if item == 1 else result - loss[i]

    return result

# the function to check if the fitvalue has some values or all of them is zero
def check(fitvalue):
    return fitvalue.count(0) != len(fitvalue)

## main function defined from here
def main():

    seed_value = int(input("enter the seed for randomization: "))
    seed(seed_value)

    n = int(input("enter the number of items: "))

    max_weight = int(input("enter the max weight: "))

    print("enter the weights: ")
    weights = list(map(int,input().split()))

    print("enter the value: ")
    value = list(map(int,input().split()))

    print("enter the loss if not taken: ")
    loss = list(map(int,input().split()))

    genes = [generate_chromosome(n) for _ in range(10)]

    sum_weight = sum(weights)

    iterations = int(input("enter the number of iteration: "))
    print(" ")

    most_fit_gene = []
    most_fit_value = 0

    for _ in range(iterations):

        newgenes = []
        fitvalue = []
        fittest_gene = 0

        for gene in genes:

            fitness_value = fitness(gene, weights, value, loss, max_weight, sum_weight)
            fitvalue.append(fitness_value)
            fittest_gene = max(fittest_gene,fitness_value)

            if not len(most_fit_gene):
                most_fit_gene = gene
                most_fit_value = fitness_value

            else:
                if most_fit_value < fitness_value:
                    most_fit_value = fitness_value
                    most_fit_gene = gene

        if check(fitvalue):

            for _ in range(5):

                # choosing the first index to breed from the current generation
                gene_a_index = choose(fitvalue)

                # choosing the second index to breed from the current generation
                gene_b_index = choose(fitvalue)

                gene_a_copy = gen_arr(genes[gene_a_index])
                gene_b_copy = gen_arr(genes[gene_b_index])

                [gene_a,gene_b] = cross_mut(gene_a_copy,gene_b_copy)

                newgenes.append(gene_a)
                newgenes.append(gene_b)
        else:
            break

        genes = newgenes



    fitvalue = []
    fittest_gene = 0

    print("Last Generation")

    for gene in genes:

            print(gene)

            fitness_value = fitness(gene,weights,value,loss,max_weight,sum_weight)
            fitvalue.append(fitness_value)
            fittest_gene = max(fittest_gene,fitness_value)

            if most_fit_value < fitness_value:
                most_fit_value = fitness_value
                most_fit_gene = gene

    print("The Finest Gene is:")
    print(most_fit_gene)
    print("The fitness of this gene is:", actual_fitness(most_fit_gene, value, loss))

if __name__ == '__main__':
    main()

