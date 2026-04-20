from collections import defaultdict

# Mapper
def mapper(line):
    parts = line.strip().split()
    name = parts[0]
    marks = int(parts[1])
    if marks >= 90:
        grade = 'A'
    elif marks >= 75:
        grade = 'B'
    elif marks >= 50:
        grade = 'C'
    else:
        grade = 'D'
    return (name, grade)

# Reducer
def reducer(mapped):
    result = {}
    for name, grade in mapped:
        result[name] = grade
    return result

# Take user input
n = int(input("Enter number of students: "))
lines = []
for i in range(n):
    entry = input("Enter name and marks (e.g. Alice 85): ")
    lines.append(entry)

mapped = [mapper(line) for line in lines]
result = reducer(mapped)

print("\nStudent Grades:")
for name, grade in result.items():
    print(f"{name}\t{grade}")
