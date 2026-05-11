import random

# Fitness function (minimize x^2)
def fitness(x):
    return x**2

def initialize_population(size):
    return [random.uniform(-10, 10) for _ in range(size)]

def calculate_affinity(pop):
    return [(x, 1 / (1 + fitness(x))) for x in pop]

def select_antibodies(pop, affinity, num_selected):
    sorted_pop = sorted(zip(pop, affinity), key=lambda x: x[1][1], reverse=True)
    return [x[0] for x in sorted_pop[:num_selected]]

def clone_antibodies(selected):
    clones = []
    for i, x in enumerate(selected):
        num_clones = len(selected) - i
        clones.extend([x] * num_clones)
    return clones

def mutate(clones, mutation_rate):
    mutated = []
    for x in clones:
        if random.random() < mutation_rate:
            x = x + random.uniform(-1, 1)
        mutated.append(x)
    return mutated

def select_next_generation(pop, mutated, size):
    combined = pop + mutated
    combined.sort(key=lambda x: fitness(x))
    return combined[:size]

def clonal_selection(pop_size=10, mutation_rate=0.2, iterations=20):
    population = initialize_population(pop_size)
    for i in range(iterations):
        affinity = calculate_affinity(population)
        selected = select_antibodies(population, affinity, pop_size // 2)
        clones = clone_antibodies(selected)
        mutated = mutate(clones, mutation_rate)
        population = select_next_generation(population, mutated, pop_size)
        best = min(population, key=fitness)
        print(f"Iteration {i}: Best = {best:.4f}, Fitness = {fitness(best):.4f}")
    return min(population, key=fitness)

best_solution = clonal_selection()
print("\nBest Solution Found:", best_solution)
print("Minimum Value:", fitness(best_solution))
