import numpy as np
import random
from sklearn.neural_network import MLPRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

# ---------------------------------------------------
# STEP 1: Generate Sample Dataset
# ---------------------------------------------------

# 100 samples with 5 input features
X = np.random.rand(100, 5)

# Target output
y = np.sum(X, axis=1) + np.random.rand(100) * 0.1

# Split dataset into training and testing
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

print("Dataset Created Successfully")
print("Training Samples:", len(X_train))
print("Testing Samples :", len(X_test))

# ---------------------------------------------------
# STEP 2: Fitness Function
# ---------------------------------------------------

def fitness(params):

    neurons, learning_rate, alpha = params

    model = MLPRegressor(
        hidden_layer_sizes=(int(neurons),),
        learning_rate_init=learning_rate,
        alpha=alpha,
        max_iter=500,
        random_state=42
    )

    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)

    mse = mean_squared_error(y_test, y_pred)

    return mse

# ---------------------------------------------------
# STEP 3: Create Individual
# ---------------------------------------------------

def create_individual():

    return [
        random.randint(10, 100),        # neurons
        random.uniform(0.001, 0.1),     # learning rate
        random.uniform(0.0001, 0.01)    # alpha
    ]

# ---------------------------------------------------
# STEP 4: Mutation Function
# ---------------------------------------------------

def mutate(individual):

    if random.random() < 0.3:
        individual[0] = random.randint(10, 100)

    if random.random() < 0.3:
        individual[1] = random.uniform(0.001, 0.1)

    if random.random() < 0.3:
        individual[2] = random.uniform(0.0001, 0.01)

    return individual

# ---------------------------------------------------
# STEP 5: Crossover Function
# ---------------------------------------------------

def crossover(parent1, parent2):

    child = [
        random.choice([parent1[0], parent2[0]]),
        random.choice([parent1[1], parent2[1]]),
        random.choice([parent1[2], parent2[2]])
    ]

    return child

# ---------------------------------------------------
# STEP 6: Initialize Population
# ---------------------------------------------------

population_size = 10

population = [
    create_individual()
    for _ in range(population_size)
]

print("\nInitial Population Created")
print("Population Size:", population_size)

# ---------------------------------------------------
# STEP 7: Genetic Algorithm Main Loop
# ---------------------------------------------------

num_generations = 10

print("\n===================================")
print("GENETIC ALGORITHM RUNNING")
print("===================================")

for generation in range(num_generations):

    # Evaluate fitness of all individuals
    scores = []

    for individual in population:
        mse = fitness(individual)
        scores.append((mse, individual))

    # Sort based on lowest MSE
    scores.sort(key=lambda x: x[0])

    # Print best result of this generation
    print(f"\nGeneration {generation}")
    print("Best MSE       :", round(scores[0][0], 6))
    print("Best Neurons   :", scores[0][1][0])
    print("Best LR        :", round(scores[0][1][1], 6))
    print("Best Alpha     :", round(scores[0][1][2], 6))

    # Select top 50%
    selected = [ind for (_, ind) in scores[:5]]

    # Create next generation
    new_population = selected.copy()

    while len(new_population) < population_size:

        parent1, parent2 = random.sample(selected, 2)

        child = crossover(parent1, parent2)

        child = mutate(child)

        new_population.append(child)

    population = new_population

# ---------------------------------------------------
# STEP 8: Final Best Solution
# ---------------------------------------------------

best_solution = min(population, key=lambda x: fitness(x))

print("\n===================================")
print("BEST PARAMETERS FOUND")
print("===================================")
print("Number of Neurons :", best_solution[0])
print("Learning Rate     :", round(best_solution[1], 6))
print("Alpha Value       :", round(best_solution[2], 6))
print("Final Best MSE    :", round(fitness(best_solution), 6))
print("===================================")
