import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris

# STEP 1: Extraction
iris = load_iris()
df = pd.DataFrame(iris.data, columns=iris.feature_names)
df['species'] = iris.target
print("Step 1 - Extracted Data:")
print(df.head())

# STEP 2: Transformation
print("\nStep 2 - Missing Values:")
print(df.isnull().sum())

# Create new column
df['sepal_area'] = df['sepal length (cm)'] * df['sepal width (cm)']

# Convert species numbers to names
df['species_name'] = df['species'].map({0: 'setosa', 1: 'versicolor', 2: 'virginica'})
print("\nTransformed Data Sample:")
print(df.head())

# STEP 3: Load
df.to_csv("iris_transformed.csv", index=False)
print("\nStep 3 - Data loaded to iris_transformed.csv")

# STEP 4: Visualization
fig, axes = plt.subplots(1, 2, figsize=(12, 5))

# Sepal Length Distribution
df['sepal length (cm)'].hist(ax=axes[0], bins=20, color='steelblue')
axes[0].set_title('Sepal Length Distribution')
axes[0].set_xlabel('Sepal Length (cm)')

# Scatter Plot
for species, color in zip(['setosa', 'versicolor', 'virginica'], ['red', 'green', 'blue']):
    subset = df[df['species_name'] == species]
    axes[1].scatter(subset['sepal length (cm)'], subset['petal length (cm)'], label=species, color=color)
axes[1].set_title('Scatter Plot: Sepal vs Petal Length')
axes[1].set_xlabel('Sepal Length')
axes[1].set_ylabel('Petal Length')
axes[1].legend()

plt.tight_layout()
plt.savefig("bi_p7_output.png")
plt.show()
print("Visualization saved to bi_p7_output.png")
