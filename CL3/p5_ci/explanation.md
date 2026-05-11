# P5 — Genetic Algorithm (Neural Network Hyperparameter Tuning)

## What is this Practical?
Uses a **Genetic Algorithm (GA)** to automatically find the best hyperparameters (neurons, learning rate, alpha) for a neural network. Instead of manually tuning or brute-force searching, the GA evolves a population of parameter sets over generations — keeping good ones and discarding bad ones.

---

## Theory

### What is a Genetic Algorithm?
A Genetic Algorithm is a **search and optimization** algorithm inspired by **Charles Darwin's theory of natural selection** — survival of the fittest. Just as nature evolves organisms to be better adapted to their environment over generations, GAs evolve candidate solutions to be better at solving a problem.

Introduced by **John Holland** in the 1970s, GAs belong to the broader family of **Evolutionary Algorithms**.

### Biological Inspiration

| Biology | Genetic Algorithm |
|---|---|
| Organism | Individual (candidate solution) |
| Population | Group of candidate solutions |
| Chromosome | Encoded solution (list of parameters) |
| Gene | One parameter value |
| Fitness | How good the solution is |
| Selection | Keeping the best individuals |
| Crossover (Reproduction) | Combining two parents to make a child |
| Mutation | Randomly changing a gene |
| Generation | One iteration of the algorithm |

### GA Flow
```
1. Initialize random population
2. Evaluate fitness of each individual
3. Select the best individuals (parents)
4. Create new individuals via crossover and mutation
5. Replace old population with new one
6. Repeat from step 2 for N generations
7. Return the best individual found
```

### Selection
Only the fittest individuals (lowest MSE here) survive to produce offspring. This ensures the population improves over time. Here, the top 50% are selected.

### Crossover
Two parents combine to produce a child. Each gene of the child is randomly chosen from either parent. This combines good traits from both parents — similar to how children inherit from both mother and father.

### Mutation
A small random change is applied to some genes with a low probability (30% here). Without mutation, the algorithm could get stuck — all individuals would eventually converge to the same solution. Mutation introduces new genetic diversity to explore new regions of the solution space.

### Fitness Function
The fitness function measures how good a candidate solution is. Here, it trains a neural network with the given hyperparameters and measures the **Mean Squared Error (MSE)** on test data. Lower MSE = better solution.

### Neural Network Hyperparameters Being Tuned
- **Neurons** — Number of neurons in the hidden layer. Too few = underfitting. Too many = overfitting or slow.
- **Learning Rate** — How fast the network adjusts weights. Too high = unstable. Too low = slow convergence.
- **Alpha** — L2 regularization penalty. Controls overfitting by penalizing large weights.

### Why Use GA for Hyperparameter Tuning?
The hyperparameter space is large and non-convex — there's no formula to find the best values directly. GA explores this space efficiently by:
- Testing many combinations in parallel (population)
- Focusing on promising regions (selection)
- Combining good solutions (crossover)
- Occasionally exploring new areas (mutation)

---

## Key Concepts

| Concept | Meaning |
|---|---|
| Individual | A list [neurons, learning_rate, alpha] |
| Population | 10 individuals evaluated together |
| Fitness | MSE of neural network with these hyperparameters |
| Selection | Keep top 5 (50%) each generation |
| Crossover | Randomly pick each gene from either parent |
| Mutation | 30% chance each gene is randomly replaced |
| MSE | Mean Squared Error — average of (predicted − actual)² |

---

## Code — Line by Line

```python
X = np.random.rand(100, 5)
y = np.sum(X, axis=1) + np.random.rand(100) * 0.1
```
Creates 100 samples with 5 features. Target y = sum of features + small noise (a simple regression problem).

```python
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
```
80% training, 20% testing. `random_state=42` ensures reproducibility.

```python
def fitness(params):
    neurons, learning_rate, alpha = params
    model = MLPRegressor(hidden_layer_sizes=(int(neurons),), learning_rate_init=learning_rate, alpha=alpha, ...)
    model.fit(X_train, y_train)
    return mean_squared_error(y_test, model.predict(X_test))
```
Builds, trains, and evaluates a neural network with the given hyperparameters. Returns MSE — lower is better.

```python
def create_individual():
    return [random.randint(10, 100), random.uniform(0.001, 0.1), random.uniform(0.0001, 0.01)]
```
Creates one random individual — 3 random hyperparameter values within defined ranges.

```python
def mutate(individual):
    if random.random() < 0.3:
        individual[0] = random.randint(10, 100)
```
Each gene has 30% chance of being replaced with a new random value. Prevents population from converging too early.

```python
def crossover(parent1, parent2):
    return [random.choice([parent1[i], parent2[i]]) for i in range(3)]
```
Each gene of the child is randomly inherited from one of the two parents.

```python
scores.sort(key=lambda x: x[0])
selected = [ind for (_, ind) in scores[:5]]
```
Sorts all individuals by MSE (ascending). Keeps the best 5 as parents.

```python
while len(new_population) < population_size:
    parent1, parent2 = random.sample(selected, 2)
    child = mutate(crossover(parent1, parent2))
    new_population.append(child)
```
Fills the next generation by repeatedly crossing and mutating pairs of parents until population size is restored.
