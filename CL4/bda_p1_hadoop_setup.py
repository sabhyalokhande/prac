# BDA Practical 1 - Hadoop Setup Simulation
# Since Hadoop requires a Linux environment, this script simulates
# the MapReduce WordCount locally using Python

from collections import defaultdict

# Simulate: echo "hello hadoop hello world" > file1.txt
text = "hello hadoop hello world"

print("=== Simulating Hadoop WordCount MapReduce ===")
print(f"Input: {text}\n")

# MAP PHASE
def mapper(line):
    return [(word, 1) for word in line.strip().split()]

mapped = mapper(text)
print("Map Output:")
for pair in mapped:
    print(f"  {pair[0]}\t{pair[1]}")

# SHUFFLE & SORT
grouped = defaultdict(list)
for word, count in sorted(mapped):
    grouped[word].append(count)

# REDUCE PHASE
def reducer(grouped):
    return {word: sum(counts) for word, counts in grouped.items()}

result = reducer(grouped)

print("\nReduce Output (hdfs dfs -cat /output/part-r-00000):")
for word, count in sorted(result.items()):
    print(f"  {word}\t{count}")
