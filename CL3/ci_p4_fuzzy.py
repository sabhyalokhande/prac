def fuzzy_union(A, B):
    return {x: max(A.get(x, 0), B.get(x, 0)) for x in set(A) | set(B)}

def fuzzy_intersection(A, B):
    return {x: min(A.get(x, 0), B.get(x, 0)) for x in set(A) | set(B)}

def fuzzy_complement(A):
    return {x: 1 - A[x] for x in A}

def fuzzy_difference(A, B):
    return {x: min(A.get(x, 0), 1 - B.get(x, 0)) for x in set(A) | set(B)}

def cartesian_product(A, B):
    return {(x, y): min(A[x], B[y]) for x in A for y in B}

def max_min_composition(R, S):
    T = {}
    for (x, y1) in R:
        for (y2, z) in S:
            if y1 == y2:
                T[(x, z)] = max(T.get((x, z), 0), min(R[(x, y1)], S[(y2, z)]))
    return T

A = {'a': 0.5, 'b': 0.7, 'c': 0.2}
B = {'b': 0.6, 'c': 0.8, 'd': 0.4}

print("A = ", A)
print("B = ", B)

R = cartesian_product(A, B)
print("Cartesian Product (AxB):")
for i in R:
    print(i, R[i])

print("\n")
print("Fuzzy Union: ", fuzzy_union(A, B))
print("Fuzzy Difference: ", fuzzy_difference(A, B))
print("Fuzzy Complement: ", fuzzy_complement(A))
print("Fuzzy Intersection: ", fuzzy_intersection(A, B))

print("\n")
C = {'x': 0.3, 'y': 0.9, 'z': 0.5}
print("C = ", C)
print("Max-Min composition on Two Fuzzy Relations:")
S = cartesian_product(B, C)
max_min = max_min_composition(R, S)
for i in max_min:
    print(i, max_min[i])
