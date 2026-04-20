import pandas as pd

# Simulate importing data from Excel / CSV (like Power BI's Get Data)
# Creates a sample products dataset and loads it

data = {
    'ProductID': [1, 2, 3, 4, 5],
    'ProductName': ['Apple', 'Banana', 'Cherry', 'Date', 'Elderberry'],
    'Category': ['Fruit', 'Fruit', 'Fruit', 'Fruit', 'Fruit'],
    'Price': [1.5, 0.5, 3.0, 2.5, 4.0],
    'Stock': [100, 200, 50, 75, 30]
}

df = pd.DataFrame(data)

# Save to CSV (simulating Excel export)
df.to_csv("products.csv", index=False)
print("Data saved to products.csv")

# Load back (simulating Power BI's Load)
loaded = pd.read_csv("products.csv")
print("\nLoaded Data:")
print(loaded.to_string(index=False))

# Basic transformations (like Power Query)
print("\nTransformed Data (Price > 1.0):")
filtered = loaded[loaded['Price'] > 1.0]
print(filtered.to_string(index=False))
