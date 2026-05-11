# P6 — Clonal Selection Algorithm

## What is this Practical?
Implements the **Clonal Selection Algorithm (CSA)** — an optimization technique inspired by how the human immune system responds to and remembers antigens. It evolves a population of candidate solutions (antibodies) to minimize the function x².

---

## Theory

### The Biological Immune System
When a pathogen (antigen) enters the body, the immune system responds by:
1. **Recognizing** — B-cells and T-cells with matching receptors are identified
2. **Cloning** — Matching cells are rapidly cloned (reproduced in large numbers)
3. **Hypermutation** — Clones are mutated at a high rate to improve binding
4. **Selection** — Clones with better affinity (stronger binding) survive and multiply
5. **Memory** — The best cells are kept as memory cells for faster future responses

This process is called **Clonal Selection** — only cells that match well are selected and cloned.

### Artificial Immune Systems (AIS)
Artificial Immune Systems are a class of computational intelligence algorithms that borrow concepts from immunology. The Clonal Selection Algorithm (CLONALG) was proposed by **de Castro and Von Zuben** in 2002.

AIS are used for:
- Optimization problems
- Pattern recognition
- Anomaly/intrusion detection
- Machine learning

### Clonal Selection Algorithm (CSA) — How It Works

```
1. Initialize a random population of antibodies (candidate solutions)
2. Calculate affinity (fitness) of each antibody
3. Select the best antibodies
4. Clone them — better antibodies get more clones
5. Hypermutate the clones (randomly modify them)
6. Select the best from original + mutated clones
7. Repeat for N iterations
```

### Affinity vs Fitness
- **Fitness** measures the raw quality of a solution (e.g., x² — lower is better)
- **Affinity** is the inverse — how well the antibody "binds" to the antigen (higher is better)
- Formula: `affinity = 1 / (1 + fitness)` — transforms minimization into maximization

### Hypermutation
Unlike genetic algorithms where mutation rate is fixed and low, in CSA the mutation is **inversely proportional to affinity**:
- High affinity (good solution) → low mutation (exploit what's working)
- Low affinity (bad solution) → high mutation (explore aggressively)

In our implementation, a fixed mutation rate is used for simplicity.

### Cloning Proportional to Affinity
Better antibodies produce more clones:
- Best antibody (index 0) gets `n` clones
- Second best gets `n-1` clones
- ...
- Worst selected gets 1 clone

This focuses computational effort on the most promising regions of the search space.

### What Problem Are We Solving?
The algorithm minimizes **f(x) = x²** — find the value of x closest to 0. This is a simple test function. The minimum is x=0, f(0)=0. The algorithm starts with random x values between -10 and 10 and evolves toward 0.

---

## Key Concepts

| Concept | Meaning |
|---|---|
| Antibody | A candidate solution (a number x) |
| Antigen | The problem — minimize x² |
| Affinity | 1/(1+fitness) — how good the antibody is |
| Cloning | Reproducing good antibodies multiple times |
| Hypermutation | Randomly modifying clones to explore nearby solutions |
| Memory Cell | Best solutions kept across generations |
| Population Size | 10 antibodies maintained each iteration |

---

## Code — Line by Line

```python
def fitness(x):
    return x**2
```
The problem to minimize. Optimal solution: x=0 where fitness=0.

```python
def initialize_population(size):
    return [random.uniform(-10, 10) for _ in range(size)]
```
Creates `size` random numbers between -10 and 10 as starting antibodies.

```python
def calculate_affinity(pop):
    return [(x, 1 / (1 + fitness(x))) for x in pop]
```
Affinity = `1/(1+x²)`. As x→0 (best), affinity→1. As |x| grows (worse), affinity→0.

```python
def select_antibodies(pop, affinity, num_selected):
    sorted_pop = sorted(zip(pop, affinity), key=lambda x: x[1][1], reverse=True)
    return [x[0] for x in sorted_pop[:num_selected]]
```
Sorts antibodies by affinity (highest first) and returns the top half.

```python
def clone_antibodies(selected):
    for i, x in enumerate(selected):
        num_clones = len(selected) - i
        clones.extend([x] * num_clones)
```
Best antibody (i=0) gets the most clones (`len(selected)`), worst gets fewest (1). More promising solutions are explored more thoroughly.

```python
def mutate(clones, mutation_rate):
    if random.random() < mutation_rate:
        x = x + random.uniform(-1, 1)
```
Each clone has a `mutation_rate` (20%) chance of being shifted by ±1. Explores solutions near the current one.

```python
def select_next_generation(pop, mutated, size):
    combined = pop + mutated
    combined.sort(key=lambda x: fitness(x))
    return combined[:size]
```
Merges original population with all mutated clones, sorts by fitness (ascending = best first), keeps only the top `size`.

```python
for i in range(iterations):
    affinity = calculate_affinity(population)
    selected = select_antibodies(population, affinity, pop_size // 2)
    clones = clone_antibodies(selected)
    mutated = mutate(clones, mutation_rate)
    population = select_next_generation(population, mutated, pop_size)
    best = min(population, key=fitness)
    print(f"Iteration {i}: Best = {best:.4f}, Fitness = {fitness(best):.4f}")
```
Main loop — runs all phases each iteration and prints the best solution found so far.
