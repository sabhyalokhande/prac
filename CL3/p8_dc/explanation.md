# P8 — DEAP Genetic Algorithm (Multiprocessing)

## What is this Practical?
Uses the **DEAP library** to run a Genetic Algorithm that minimizes the function f(x₁, x₂, x₃) = x₁² + x₂² + x₃². DEAP provides ready-made GA tools, and Python's `multiprocessing` module is used to evaluate fitness in parallel across CPU cores.

---

## Theory

### DEAP — Distributed Evolutionary Algorithms in Python
DEAP is an open-source Python framework for evolutionary computation. It provides:
- Ready-made genetic operators (crossover, mutation, selection)
- A flexible toolbox to register and combine operators
- Support for parallel execution via multiprocessing
- Tools for statistics, logging, and hall of fame tracking

It follows a **component-based design** — you register what functions to use for each operation, then DEAP calls them in the right order.

### Fitness Function and Minimization
The function to minimize is:
```
f(x₁, x₂, x₃) = x₁² + x₂² + x₃²
```
This is a **sphere function** — a standard benchmark in optimization. Its global minimum is at (0, 0, 0) where f = 0.

DEAP uses a **weights** system to define optimization direction:
- `weights=(-1.0,)` → minimize (negative weight penalizes higher values)
- `weights=(+1.0,)` → maximize

### Blend Crossover (cxBlend)
In blend crossover with parameter α:
- For each gene, the child's value is picked randomly from the range `[min(p1, p2) - α·d, max(p1, p2) + α·d]`
- where `d = |p1 - p2|` (distance between parents)
- α=0.5 means the child can explore slightly beyond the parents' range
- This allows exploration while staying close to the parents

### Gaussian Mutation (mutGaussian)
Adds random noise from a Gaussian (normal) distribution to each gene:
- `mu=0` → mean of the noise is zero (no systematic bias)
- `sigma=1` → standard deviation of 1 (moderate perturbation)
- `indpb=0.2` → each gene has 20% probability of being mutated

### Tournament Selection (selTournament)
In tournament selection:
1. Randomly pick `tournsize` individuals from the population
2. The one with the best fitness wins and is selected
3. Repeat until enough parents are selected
- `tournsize=3` means 3 individuals compete each time
- Larger tournament size → stronger selection pressure → faster convergence but less diversity

### Multiprocessing for Parallel Fitness Evaluation
Evaluating fitness for each individual is independent — you don't need individual A's result to compute individual B's fitness. This is called **embarrassingly parallel**.

`multiprocessing.Pool()` creates a pool of worker processes (one per CPU core). `pool.map(func, population)` distributes the population across all cores simultaneously — significantly faster on multi-core machines.

The `if __name__ == "__main__":` guard is **required** on Windows when using multiprocessing, because Windows uses `spawn` to create new processes and needs to safely import the main module without re-running it.

### varAnd — Variation Operator
`algorithms.varAnd(population, toolbox, cxpb=0.5, mutpb=0.1)`:
- `cxpb=0.5` — each pair of individuals has 50% chance of crossover
- `mutpb=0.1` — each individual has 10% chance of mutation
- Returns a new list of offspring (original population is not modified)

---

## Key Concepts

| Concept | Meaning |
|---|---|
| DEAP | Python library for evolutionary algorithms |
| Individual | A list [x₁, x₂, x₃] with an attached fitness value |
| `weights=(-1.0,)` | Tells DEAP to minimize fitness |
| `cxBlend` | Blend crossover — child picks value from parents' range + α |
| `mutGaussian` | Adds Gaussian noise to genes |
| `selTournament` | Selects best from random tournament of 3 |
| `multiprocessing.Pool` | Evaluates all individuals in parallel across CPU cores |
| `varAnd` | Applies crossover and mutation to produce offspring |
| Sphere function | f = Σxᵢ² — standard optimization benchmark |

---

## Code — Line by Line

```python
def eval_func(individual):
    return sum(x**2 for x in individual),
```
Fitness function — returns sum of squares. The trailing comma creates a tuple, required by DEAP's fitness system.

```python
creator.create("FitnessMin", base.Fitness, weights=(-1.0,))
```
Creates a fitness class. `weights=(-1.0,)` means DEAP will try to minimize (it internally multiplies fitness by weight, so lower values become "better").

```python
creator.create("Individual", list, fitness=creator.FitnessMin)
```
Creates an Individual class — a Python list with an attached `fitness` attribute.

```python
toolbox.register("attr_float", random.uniform, -5.0, 5.0)
toolbox.register("individual", tools.initRepeat, creator.Individual, toolbox.attr_float, n=3)
toolbox.register("population", tools.initRepeat, list, toolbox.individual)
```
Sets up how to build genes (random float), individuals (3 genes), and populations (list of individuals).

```python
toolbox.register("mate", tools.cxBlend, alpha=0.5)
toolbox.register("mutate", tools.mutGaussian, mu=0, sigma=1, indpb=0.2)
toolbox.register("select", tools.selTournament, tournsize=3)
```
Registers the genetic operators. DEAP will call these during evolution.

```python
pool = multiprocessing.Pool()
toolbox.register("map", pool.map)
```
Creates a worker process pool. Replaces Python's built-in `map` with `pool.map` so DEAP evaluates fitness in parallel.

```python
population = toolbox.population(n=50)
fitnesses = list(toolbox.map(toolbox.evaluate, population))
for ind, fit in zip(population, fitnesses):
    ind.fitness.values = fit
```
Creates 50 individuals, evaluates all fitnesses in parallel, and assigns them to each individual.

```python
offspring = algorithms.varAnd(population, toolbox, cxpb=0.5, mutpb=0.1)
```
Produces offspring by applying crossover (50% chance per pair) and mutation (10% chance per individual).

```python
population = toolbox.select(offspring, k=len(population))
```
Selects the best 50 individuals from offspring using tournament selection to form the next generation.

```python
pool.close()
pool.join()
```
Shuts down worker processes. `close()` stops accepting new tasks. `join()` waits for all workers to finish before continuing.
