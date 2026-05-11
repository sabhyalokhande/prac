# P7 — AIRS (Artificial Immune Recognition System)

## What is this Practical?
Implements **AIRS** — an Artificial Immune System classifier. It trains a set of "detector" cells on labeled data and classifies new samples by finding the most similar detector — inspired by how the immune system recognizes and remembers pathogens.

---

## Theory

### Artificial Immune Systems (AIS)
Artificial Immune Systems are a class of machine learning algorithms modeled on the **vertebrate immune system**. They are used for:
- Classification
- Anomaly/intrusion detection
- Optimization
- Clustering

### How the Real Immune System Works
1. **Antigens** — foreign substances (viruses, bacteria) that invade the body
2. **Antibodies / Lymphocytes** — cells that recognize specific antigens
3. **Clonal Selection** — when an antigen is detected, matching cells clone themselves
4. **Affinity Maturation** — clones mutate to improve their recognition ability
5. **Memory Cells** — after the infection, some cells are kept as long-term memory for faster future response

### AIRS — Artificial Immune Recognition System
AIRS was proposed by **Andrew Watkins** in 2002. It is a supervised learning algorithm — it learns from labeled training data and classifies new (unseen) data.

#### How AIRS Works:
1. **Training**: Select a subset of training samples as "detectors" (memory cells). These represent the learned patterns.
2. **Mutation**: Slightly randomize detectors to improve generalization (avoid memorizing exact training points).
3. **Prediction**: For each new test sample, find the closest detector using Euclidean distance. Assign the detector's class label to the test sample.

This is essentially a **1-Nearest Neighbour classifier** with a mutation step during training.

### Euclidean Distance
The distance between two points in n-dimensional space:
```
d = sqrt((x1-y1)² + (x2-y2)² + ... + (xn-yn)²)
```
In our case, each data sample has 10 features, so distance is calculated in 10-dimensional space. Closer distance = more similar samples.

`np.linalg.norm(a - b)` computes this directly.

### Why Mutation During Training?
If detectors are exact copies of training samples, the model memorizes training data but may fail on slightly different test data (overfitting). Adding small random noise to detectors makes them more general — they cover a small neighborhood rather than a single point.

### Classification Accuracy
```
Accuracy = (number of correct predictions) / (total predictions)
```
`np.mean(y_pred == y_test)` computes this — compares predicted and actual labels element-wise and averages the boolean results (True=1, False=0).

### Dummy Data
Since no real dataset is used, the program generates:
- 100 random samples with 10 features each
- Random binary labels (0=healthy, 1=damaged)

Because labels are randomly assigned, accuracy will be around 50% — this is expected and normal. The goal is to demonstrate the algorithm, not achieve high accuracy.

---

## Key Concepts

| Concept | Meaning |
|---|---|
| Antigen | The problem input — test sample to classify |
| Detector | A selected training sample acting as a memory cell |
| Affinity | How well a detector matches a sample (inverse of distance) |
| Mutation | Small random noise added to detectors during training |
| Euclidean Distance | Straight-line distance in multi-dimensional feature space |
| 1-NN Classification | Classify based on the single closest known sample |
| Accuracy | Fraction of test samples correctly classified |

---

## Code — Line by Line

```python
def generate_dummy_data(samples=100, features=10):
    X = np.random.rand(samples, features)
    y = np.random.randint(0, 2, size=samples)
    return X, y
```
Generates 100 random samples with 10 features. Labels are randomly 0 or 1 (binary classification).

```python
class AIRS:
    def __init__(self, num_detectors=10, mutation_rate=0.1):
```
Initializes with 10 detectors and 10% mutation rate.

```python
    def train(self, X, y):
        indices = np.random.choice(len(X), self.num_detectors, replace=False)
        self.detectors = X[indices]
        self.detector_labels = y[indices]
```
Randomly selects 10 training samples as detectors. `replace=False` ensures no sample is picked twice.

```python
        for i in range(len(self.detectors)):
            if np.random.rand() < self.mutation_rate:
                self.detectors[i] += np.random.normal(0, 0.1, size=self.detectors[i].shape)
```
Each detector has 10% chance of being mutated — small Gaussian noise (mean=0, std=0.1) added to all its feature values.

```python
    def predict(self, X):
        for sample in X:
            distances = np.linalg.norm(self.detectors - sample, axis=1)
```
For each test sample, computes Euclidean distance to all 10 detectors simultaneously. `axis=1` means compute distance row-by-row (one distance per detector).

```python
            idx = np.argmin(distances)
            predictions.append(self.detector_labels[idx])
```
`argmin` returns the index of the closest detector. The test sample is assigned that detector's label.

```python
split = int(0.8 * len(X))
X_train, X_test = X[:split], X[split:]
```
Manual 80/20 train-test split. First 80 samples for training, last 20 for testing.

```python
accuracy = np.mean(y_pred == y_test)
print("Accuracy:", accuracy)
```
Element-wise comparison returns [True, False, True, ...]. `np.mean` converts to [1, 0, 1, ...] and averages. Result is the fraction of correct predictions.
