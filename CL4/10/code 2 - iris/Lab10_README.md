# Lab Practical 10 — Data Classification using Logistic Regression (Python + Jupyter)

**Aim:** Perform the data classification algorithm using any Classification algorithm.

**Algorithm used:** Logistic Regression  
**Dataset:** `Iris.csv`

---

## How to Open Jupyter Notebook

1. Press **Windows** key → search **Jupyter Notebook** → click to open
2. A browser tab opens at `http://localhost:8888`
3. Navigate to your folder → click **New** → **Python 3**

---

## STEP 1: Import Libraries

```python
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay
import matplotlib.pyplot as plt
```

---

## STEP 2: Load Dataset

```python
df = pd.read_csv("D:/College/BE/Dataset/Iris.csv")
df.head()
```

Output (first 5 rows):

| | SepalLengthCm | SepalWidthCm | PetalLengthCm | PetalWidthCm | Species |
|---|---|---|---|---|---|
| 0 | 5.1 | 3.5 | 1.4 | 0.2 | Iris-setosa |
| 1 | 4.9 | 3.0 | 1.4 | 0.2 | Iris-setosa |
| 2 | 4.7 | 3.2 | 1.3 | 0.2 | Iris-setosa |
| 3 | 4.6 | 3.1 | 1.5 | 0.2 | Iris-setosa |
| 4 | 5.0 | 3.6 | 1.4 | 0.2 | Iris-setosa |

---

## STEP 3: Prepare Data

```python
X = df.drop("Species", axis=1)
y = df["Species"]
y.head()
```

Output:
```
0    Iris-setosa
1    Iris-setosa
2    Iris-setosa
3    Iris-setosa
4    Iris-setosa
Name: Species, dtype: object
```

- `X` → all feature columns (SepalLengthCm, SepalWidthCm, PetalLengthCm, PetalWidthCm)
- `y` → target column (Species)

---

## STEP 4: Convert Labels

```python
from sklearn.preprocessing import LabelEncoder

le = LabelEncoder()
y = le.fit_transform(y)
print(y)
```

Converts string species names to numbers:
- `Iris-setosa` → `0`
- `Iris-versicolor` → `1`
- `Iris-virginica` → `2`

---

## STEP 5: Split Data and Apply Classification Algorithm

```python
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)

model = LogisticRegression(max_iter=200)
model.fit(X_train, y_train)
```

- `test_size=0.3` → 70% training data, 30% testing data
- `max_iter=200` → allows up to 200 iterations for convergence

---

## STEP 6: Prediction

```python
y_pred = model.predict(X_test)
```

Predicts the species class (0, 1, or 2) for each test sample.

---

## STEP 7: Evaluation

```python
cm = confusion_matrix(y_test, y_pred)
disp = ConfusionMatrixDisplay(confusion_matrix=cm)
disp.plot(cmap='Blues')
plt.show()
```

Expected Confusion Matrix output:
```
Predicted:   0    1    2
True 0:     12    0    0
True 1:      0   17    0
True 2:      0    0   16
```

- Diagonal values (12, 17, 16) = correctly classified samples
- Off-diagonal values = misclassified samples
- All zeros off-diagonal → **100% accuracy** on this run

---

## Result

Logistic Regression classification performed on the Iris dataset:
- **Extracted** — Iris.csv loaded with 150 rows, 5 columns
- **Prepared** — Features (X) and labels (y) separated; labels encoded as 0, 1, 2
- **Trained** — LogisticRegression model trained on 70% of data
- **Predicted** — Species predicted for 30% test data
- **Evaluated** — Confusion matrix displayed showing classification accuracy
