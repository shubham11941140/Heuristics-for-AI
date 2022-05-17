# Approach of the problem

The length of the gene is equal to the available number of objects and the value of the chromosomes in the gene will be 1 or 0 based on selection of the object, like if we are picking the object then the value of chromosomes will be 1 and 0 otherwise.

## How the fitness is calculated

Fitness of the gene is based on the sum of the values of the object taken,loss for the object not taken and total weight of the bag

The pseudo code of the function is given below

fitness_function()
	if(total weight of the bag is greater than max  OR total value less than 0)
	then fitness = 0
	else
	then fitness = ((total values * (sum of weights of all object)) + weight)

The above fitness function give more priority to the gene with lowest weight if compared to all the gene with same value

## The function for choosing

The best gene is chosen based on the Roulette selection technique, in which the gene with more fitness level has relatively high probability of getting chosen.

## Cross-Over and Mutation

For cross over two genes are selected from the current generation and they are randomly sliced from between and the the first part is swapped and the for each chromosome in both genes we do mutation with probability of 0.1

# Input

1. first line is a single integer denoting the seed of the randomization function
2. second line is a single integer denoting the number of items available
3. third line is a single integer denoting the maximum weight of bag
4. fourth line is an array of integers denoting the weight of 1st item, 2nd item, 3rd item and so on.
5. fifth line is an array of integers denoting the value of 1st item, 2nd item, 3rd item and so on.
6. sixth line is an array of integers denoting the loss for not taking the 1st item, 2nd item, 3rd item and so on.
7. seventh line is a single integer denoting the number of iteration you want

### Refer to the input file ```in.txt``` that refers to the input as per the question given

# Execution

```
    python3 genetic.py
```
