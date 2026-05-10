import numpy as np
from sklearn.neural_network import MLPRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
import random

# Generate sample data
X = np.random.rand(100, 5)
y = np.sum(X, axis=1) + np.random.rand(100) * 0.1

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Fitness function
def fitness(params):
    pop_size, crossover_rate, mutation_rate = params
    model = MLPRegressor(hidden_layer_sizes=(50,), max_iter=300, random_state=42)
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    mse = mean_squared_error(y_test, y_pred)
    return mse

# Genetic Algorithm
def create_individual():
    return [
        random.randint(50, 100),
        random.uniform(0.6, 0.9),
        random.uniform(0.01, 0.1)
    ]

def mutate(ind):
    if random.random() < 0.3:
        ind[0] = random.randint(50, 100)
    if random.random() < 0.3:
        ind[1] = random.uniform(0.6, 0.9)
    if random.random() < 0.3:
        ind[2] = random.uniform(0.01, 0.1)
    return ind

def crossover(p1, p2):
    return [
        random.choice([p1[0], p2[0]]),
        random.choice([p1[1], p2[1]]),
        random.choice([p1[2], p2[2]])
    ]

# GA Main Loop
population = [create_individual() for _ in range(10)]

for generation in range(10):
    scores = [(fitness(ind), ind) for ind in population]
    scores.sort(key=lambda x: x[0])
    print(f"Generation {generation} Best MSE:", scores[0][0])

    selected = [ind for (_, ind) in scores[:5]]
    new_population = selected.copy()
    while len(new_population) < 10:
        p1, p2 = random.sample(selected, 2)
        child = crossover(p1, p2)
        child = mutate(child)
        new_population.append(child)
    population = new_population

best = min(population, key=lambda x: fitness(x))
print("\nBest Parameters Found:")
print("Population Size:", best[0])
print("Crossover Rate:", best[1])
print("Mutation Rate:", best[2])
