from collections import defaultdict

# Simulate input file
text = "Bus, Car, bus, car, train, car, bus, BUS"

# Mapper
def mapper(line):
    words = line.split(",")
    return [(word.upper().strip(), 1) for word in words]

# Reducer
def reducer(mapped):
    counts = defaultdict(int)
    for word, count in mapped:
        counts[word] += count
    return counts

# Run
mapped = mapper(text)
result = reducer(mapped)

print("Word Frequency Count:")
for word, count in sorted(result.items()):
    print(f"{word}\t{count}")
