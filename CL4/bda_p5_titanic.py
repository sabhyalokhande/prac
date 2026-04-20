import csv
from collections import defaultdict

# Download Titanic dataset if not present
import os
import urllib.request

csv_file = "Titanic.csv"
if not os.path.exists(csv_file):
    url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
    print("Downloading Titanic dataset...")
    urllib.request.urlretrieve(url, csv_file)
    print("Downloaded.")

# --- Job 1: Average age of people who DIED, by gender ---
gender_age = defaultdict(list)

with open(csv_file, newline='') as f:
    reader = csv.DictReader(f)
    for row in reader:
        if row['Survived'] == '0' and row['Age']:
            try:
                age = int(float(row['Age']))
                gender_age[row['Sex']].append(age)
            except:
                pass

print("Average Age of People Who Died (by Gender):")
for gender, ages in gender_age.items():
    print(f"  {gender}: {sum(ages)//len(ages)}")

# --- Job 2: Count survivors per class ---
class_survivors = defaultdict(int)

with open(csv_file, newline='') as f:
    reader = csv.DictReader(f)
    for row in reader:
        if row['Survived'] == '1':
            class_survivors[f"Class_{row['Pclass']}"] += 1

print("\nSurvivors Per Class:")
for cls, count in sorted(class_survivors.items()):
    print(f"  {cls}: {count}")
