# Lab Practical 7 — ETL Process with Iris Dataset (Python + Jupyter)

**Aim:** Perform the Extraction, Transformation and Loading (ETL) process on the Iris dataset using Python (pandas and matplotlib) in Jupyter Notebook.

---

## How to Open Jupyter Notebook

1. Press **Windows** key → search **Jupyter Notebook** → click to open
2. A browser tab opens automatically at `http://localhost:8888`
3. Navigate to your working folder → click **New** → **Python 3** to create a new notebook

---

## Dataset

- **File:** `Iris.csv`
- **Path used in code:** `D:/College/BE/Dataset/Iris.csv`

Columns: `Id`, `SepalLengthCm`, `SepalWidthCm`, `PetalLengthCm`, `PetalWidthCm`, `Species`

---

## STEP 1: Extraction

```python
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("D:/College/BE/Dataset/Iris.csv")
df.head()
```

This loads the Iris CSV file into a DataFrame and displays the first 5 rows.

---

## STEP 2: Transformation

### (A) Check for Missing Values

```python
print(df.isnull().sum())
```

Expected output — all zeros (no missing values in Iris dataset):
```
Id                 0
SepalLengthCm      0
SepalWidthCm       0
PetalLengthCm      0
PetalWidthCm       0
Species            0
dtype: int64
```

---

### (B) Create New Column — Petal Area

```python
df['PetalArea'] = df['PetalLengthCm'] * df['PetalWidthCm']
```

Adds a new `PetalArea` column = `PetalLengthCm × PetalWidthCm`

---

### (C) Clean Species Names

```python
df['Species'] = df['Species'].str.replace('Iris-', '')
```

Converts species names from `Iris-setosa`, `Iris-versicolor`, `Iris-virginica` → `setosa`, `versicolor`, `virginica`

---

## STEP 3: Loading

```python
df.to_csv("D:/College/BE/Dataset/iris_cleaned.csv", index=False)
```

Saves the transformed DataFrame (with `PetalArea` column and cleaned `Species` names) to a new CSV file.

---

## STEP 4: Visualization

### (A) Histogram — Sepal Length Distribution

```python
plt.hist(df['SepalLengthCm'])
plt.title("Sepal Length Distribution")
plt.xlabel("Sepal Length (cm)")
plt.ylabel("Frequency")
plt.show()
```

---

### (B) Scatter Plot — Sepal vs Petal Length

```python
plt.scatter(df['SepalLengthCm'], df['PetalLengthCm'])
plt.title("Sepal vs Petal Length")
plt.xlabel("Sepal Length (cm)")
plt.ylabel("Petal Length (cm)")
plt.show()
```

---

## Result

ETL process completed using Python on the Iris dataset:
- **Extracted** — Iris.csv loaded into a pandas DataFrame
- **Transformed** — checked missing values (none found), created `PetalArea` column, cleaned `Species` names
- **Loaded** — cleaned data saved as `iris_cleaned.csv`
- **Visualized** — histogram of Sepal Length and scatter plot of Sepal vs Petal Length
