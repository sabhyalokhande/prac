import pandas as pd
import sqlite3
from sklearn.datasets import load_iris

# STEP 1: Extraction
iris = load_iris()
df = pd.DataFrame(iris.data, columns=['sepal_length', 'sepal_width', 'petal_length', 'petal_width'])
df['species'] = iris.target
print("Step 1 - Extraction:")
print(df.head())

# STEP 2: Transformation
# (A) Remove unnecessary columns
df = df[['sepal_length', 'petal_length', 'petal_width', 'species']]
print("\n(A) After removing columns:")
print(df.head())

# (B) Handle missing values (replace with mean)
df['sepal_length'] = df['sepal_length'].fillna(df['sepal_length'].mean())
df['petal_length'] = df['petal_length'].fillna(df['petal_length'].mean())
print("\n(B) After handling missing values:")
print(df.isnull().sum())

# (C) Create new column
df['petal_ratio'] = df['petal_length'] / df['petal_width']
print("\n(C) New column 'petal_ratio' added")
print(df.head())

# STEP 3: Loading into SQLite database
conn = sqlite3.connect("lab_database.db")
df.to_sql("iris", conn, if_exists="replace", index=False)
print("\nStep 3 - Data loaded into SQLite database: lab_database.db")

# STEP 4: Database Construction - query the database
print("\nStep 4 - Database Query Result:")
result = pd.read_sql("SELECT species, AVG(petal_length) as avg_petal FROM iris GROUP BY species", conn)
result['species'] = result['species'].map({0: 'setosa', 1: 'versicolor', 2: 'virginica'})
print(result)

conn.close()
