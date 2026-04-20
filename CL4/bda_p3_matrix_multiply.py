from collections import defaultdict

# Matrix M (row, col, value)
M = [(0,0,1),(0,1,2),(0,2,3),(1,0,4),(1,1,5),(1,2,6)]
# Matrix N (row, col, value)
N = [(0,0,7),(0,1,8),(1,0,9),(1,1,10),(2,0,11),(2,1,12)]

n_cols_N = 2

# Mapper
def mapper(M, N):
    mapped = []
    for (i, j, val) in M:
        for k in range(n_cols_N):
            mapped.append(((i, k), ('M', j, val)))
    for (i, j, val) in N:
        for r in range(2):  # rows of M
            mapped.append(((r, j), ('N', i, val)))
    return mapped

# Reducer
def reducer(mapped):
    grouped = defaultdict(list)
    for key, val in mapped:
        grouped[key].append(val)

    result = {}
    for (i, k), values in grouped.items():
        m_vals = {}
        n_vals = {}
        for item in values:
            if item[0] == 'M':
                m_vals[item[1]] = item[2]
            else:
                n_vals[item[1]] = item[2]
        total = sum(m_vals.get(j, 0) * n_vals.get(j, 0) for j in range(100))
        result[(i, k)] = total
    return result

mapped = mapper(M, N)
result = reducer(mapped)

print("Matrix Multiplication Result (MxN):")
for key in sorted(result):
    print(f"({key[0]},{key[1]})\t{result[key]}")
