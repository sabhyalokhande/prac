# Lab Practical 7 — Data Visualization from ETL Process (Python)

**Aim:** Data Visualization from Extraction, Transformation and Loading (ETL) Process using Python (Pandas + Matplotlib) on Superstore dataset.

---

## How to Open Jupyter Notebook

1. Open terminal / Anaconda Prompt
2. Navigate to your working folder:
   ```bash
   cd C:\Users\YourName\Documents\lab7
   ```
3. Launch Jupyter:
   ```bash
   jupyter notebook
   ```
4. Browser opens at `http://localhost:8888`
5. Click **New** → **Python 3 (ipykernel)** to create a new notebook
6. Place `Superstore.csv` in the same folder before running

---

## Prerequisites

Dataset required: `Superstore.csv` (place in the same folder as the notebook)

---

## Step 1: Extract — Load Raw Data from CSV

```python
import pandas as pd
import matplotlib.pyplot as plt

# EXTRACT - Load raw data from CSV
df = pd.read_csv("Superstore.csv", encoding='latin1')

print("Shape of data:", df.shape)
print("\nFirst 5 rows:")
df.head()
```

**Output:**
```
Shape of data: (9994, 21)
```

---

## Step 2: Transform

### Check Missing Values

```python
# Check missing values
print("Missing values:\n", df.isnull().sum())

# Drop rows with null values
df = df.dropna()

# Select only required columns
df = df[['Category', 'Sub-Category', 'Sales', 'Profit', 'Quantity']]
```

**Output:** All columns show 0 missing values.

---

### Remove Duplicates

```python
df = df.drop_duplicates()

print("\nCleaned Data Shape:", df.shape)
print(df.head())
```

**Output:**
```
Cleaned Data Shape: (7729, 5)

          Category Sub-Category      Sales      Profit  Quantity
0        Furniture    Bookcases   261.9600     41.9136         2
1        Furniture       Chairs   731.9400    219.5820         3
2  Office Supplies       Labels    14.6200      6.8714         2
3        Furniture       Tables   957.5775   -383.0310         5
4  Office Supplies      Storage    22.3680      2.5164         2
```

---

## Step 3: Load — Save Cleaned Data

```python
# LOAD - Save cleaned data to new CSV
df.to_csv("Superstore_cleaned.csv", index=False)

print("Cleaned data loaded/saved successfully!")
```

**Output:**
```
Cleaned data loaded/saved successfully!
```

---

## Step 4: Visualization

### Chart 1: Total Sales by Category (Bar Chart)

```python
category_sales = df.groupby('Category')['Sales'].sum()

plt.figure(figsize=(8, 5))
plt.bar(category_sales.index, category_sales.values, color=['steelblue', 'orange', 'green'])
plt.title('Total Sales by Category')
plt.xlabel('Category')
plt.ylabel('Total Sales')
plt.tight_layout()
plt.show()
```

Shows total sales for: **Furniture**, **Office Supplies**, **Technology**

---

### Chart 2: Sales vs Profit by Category (Line Chart)

```python
category_profit = df.groupby('Category')['Profit'].sum()

plt.figure(figsize=(8, 5))
plt.plot(category_sales.index, category_sales.values, marker='o', label='Sales', color='blue')
plt.plot(category_profit.index, category_profit.values, marker='s', label='Profit', color='red')
plt.title('Sales vs Profit by Category')
plt.xlabel('Category')
plt.ylabel('Amount')
plt.legend()
plt.tight_layout()
plt.show()
```

Compares **Sales** (blue line) vs **Profit** (red line) across all three categories.

---

## Full Code

```python
import pandas as pd
import matplotlib.pyplot as plt

# STEP 1: EXTRACT
df = pd.read_csv("Superstore.csv", encoding='latin1')
print("Shape of data:", df.shape)
print("\nFirst 5 rows:")
print(df.head())

# STEP 2: TRANSFORM
print("Missing values:\n", df.isnull().sum())
df = df.dropna()
df = df[['Category', 'Sub-Category', 'Sales', 'Profit', 'Quantity']]
df = df.drop_duplicates()
print("\nCleaned Data Shape:", df.shape)
print(df.head())

# STEP 3: LOAD
df.to_csv("Superstore_cleaned.csv", index=False)
print("Cleaned data loaded/saved successfully!")

# STEP 4: VISUALIZE
category_sales = df.groupby('Category')['Sales'].sum()
category_profit = df.groupby('Category')['Profit'].sum()

# Bar Chart - Total Sales by Category
plt.figure(figsize=(8, 5))
plt.bar(category_sales.index, category_sales.values, color=['steelblue', 'orange', 'green'])
plt.title('Total Sales by Category')
plt.xlabel('Category')
plt.ylabel('Total Sales')
plt.tight_layout()
plt.show()

# Line Chart - Sales vs Profit by Category
plt.figure(figsize=(8, 5))
plt.plot(category_sales.index, category_sales.values, marker='o', label='Sales', color='blue')
plt.plot(category_profit.index, category_profit.values, marker='s', label='Profit', color='red')
plt.title('Sales vs Profit by Category')
plt.xlabel('Category')
plt.ylabel('Amount')
plt.legend()
plt.tight_layout()
plt.show()
```

---

## Run

```bash
python Lab7_etl_visualization.py
```

> If running headless (no display):
> ```bash
> MPLBACKEND=Agg python Lab7_etl_visualization.py
> ```

---

## Result

ETL pipeline completed on Superstore dataset:
- **Extracted** 9994 rows × 21 columns from CSV
- **Transformed** — dropped nulls, removed duplicates, selected 5 key columns → 7729 rows
- **Loaded** cleaned data to `Superstore_cleaned.csv`
- **Visualized** — Bar chart (Sales by Category) and Line chart (Sales vs Profit by Category)
