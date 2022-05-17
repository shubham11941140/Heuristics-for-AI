# Heuristics-for-AI
Contains a variety of heuristic algorithms to solve some real-world problems.

## N-Puzzle

![image](https://user-images.githubusercontent.com/63910248/168763166-29a5b5db-172b-4031-a1c3-8bab69edf08a.png)

### Solution using BFS

![image](https://user-images.githubusercontent.com/63910248/168763617-c422d095-abb9-44e7-ab15-2029c431d3bd.png)
![image](https://user-images.githubusercontent.com/63910248/168763691-3b0d78d0-b913-4c54-93be-d1d32db9e967.png)

### Solution using DFS

![image](https://user-images.githubusercontent.com/63910248/168765541-b4e2158e-6820-450c-ac39-ee23bc0f550b.png)

### Solution using A*

![image](https://user-images.githubusercontent.com/63910248/168765847-0b9adbdb-d2b8-432a-b3f1-769f214c0665.png)

## Robot Movement

![image](https://user-images.githubusercontent.com/63910248/168768567-db97fbc2-1cb8-44a8-bc71-b3e32a78045a.png)

### Solution using A*

![image](https://user-images.githubusercontent.com/63910248/168769138-e797bd05-d489-4d56-a993-aadef7c18fde.png)

## Optimal Tic Tac Toe

![image](https://user-images.githubusercontent.com/63910248/168779114-a20dfa29-e2f3-4479-ad54-76e775ca6e92.png)

### Optimal Scoring at each level

![image](https://user-images.githubusercontent.com/63910248/168779270-5e3ac8ae-eadb-4959-9d45-89d2a304d082.png)

## Moon Rover (Travelling Salesman Problem)

![image](https://user-images.githubusercontent.com/63910248/168780682-2be36098-3da2-4b4f-bb73-2587aec57eb0.png)

### Optimal Solution

![image](https://user-images.githubusercontent.com/63910248/168780927-6ad24490-3072-479b-b07b-d5c93cdd9258.png)

## Genetic Algorithm

![image](https://user-images.githubusercontent.com/63910248/168784837-957b94ad-b862-4d69-93c4-cf675c9fdecc.png)

**We need to maximise the survival points**

**Ensure we properly represent the chromosomes, fitness function, crossover, mutation etc**

## Genetic Algorithm Solution Approach

The length of the gene is equal to the available number of objects and the value of the chromosomes in the gene will be 1 or 0 based on selection of the object, like if we are picking the object then the value of chromosomes will be 1 and 0 otherwise.

## How the fitness is calculated

Fitness of the gene is based on the sum of the values of the object taken,loss for the object not taken and total weight of the bag

The **Pseudo Code** of the function is given below
```
fitness_function()

	  if(total weight of the bag is greater than max  OR total value less than 0)
	      then fitness = 0
	  else
	      then fitness = ((total values * (sum of weights of all object)) + weight)
```
The above fitness function give more priority to the gene with lowest weight if compared to all the gene with same value

## The function for choosing

The best gene is chosen based on the Roulette selection technique, in which the gene with more fitness level has relatively high probability of getting chosen.

## Cross-Over and Mutation

For cross over two genes are selected from the current generation and they are randomly sliced from between and the the first part is swapped and the for each chromosome in both genes we do mutation with probability of 0.1

### Solution:

![image](https://user-images.githubusercontent.com/63910248/168785958-eaa8eb6b-f9cc-4755-8b86-04c17f6639ab.png)

## Constraint Satisfaction Problem - Sudoku Solver

![image](https://user-images.githubusercontent.com/63910248/168803357-a6e226ec-9b6c-4c6b-8b11-e63492caa67e.png)

### Solution:

![image](https://user-images.githubusercontent.com/63910248/168803465-06814d3b-ff74-435d-b0d6-ef1b311efeea.png)

## Bayesian Belief Network

![image](https://user-images.githubusercontent.com/63910248/168805640-a13c2f9d-6707-4a0f-9292-fca9247b8255.png)

![image](https://user-images.githubusercontent.com/63910248/168805958-9b4384b9-63be-49f6-8b12-7086b4559fbe.png)

### Solution:

![image](https://user-images.githubusercontent.com/63910248/168806073-3ce7af07-a541-4d78-ad75-e19d5fc4817d.png)

**Pen Paper solution has been attached for reference, can verify the solution from the same**

## SATPLAN

![image](https://user-images.githubusercontent.com/63910248/168809353-99aff970-f45c-4e2f-8bbb-8c7c36080968.png)

### Solution:

**DIMACS file is generated at every iteration till solution is obtained**

**SAT Solver out file is generated at every iteration till solution is obtained (MiniSAT Open-Source Solver used)**

#### Final Plan:

![Final Plan Problem Solution](https://user-images.githubusercontent.com/63910248/168809552-c4a31b41-e3d0-43a8-b7f0-98116ef889eb.PNG)


