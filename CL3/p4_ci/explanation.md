# P4 — Fuzzy Logic Operations

## What is this Practical?
Implements basic **fuzzy set operations** — union, intersection, complement, difference, Cartesian product, and max-min composition. Unlike classical sets where an element either fully belongs or doesn't, fuzzy sets allow partial membership.

---

## Theory

### Classical (Crisp) Sets vs Fuzzy Sets
In classical set theory, membership is binary:
- An element either belongs (1) or doesn't (0)
- Example: "tall" — a person is either tall or not tall

In real life, this is too rigid. Is a person who is 5'10" tall? What about 5'9"? Fuzzy sets solve this by allowing **degrees of membership**.

### Fuzzy Sets
A fuzzy set A over a universe X is defined by a **membership function** μ_A(x) that maps each element to a value in [0, 1]:
- μ_A(x) = 0 → x does not belong to A at all
- μ_A(x) = 1 → x fully belongs to A
- μ_A(x) = 0.7 → x belongs to A with 70% degree

Example:
```
A = {'cold': 0.9, 'warm': 0.3, 'hot': 0.1}
```
Represents how much each temperature label belongs to the fuzzy set "cold weather".

### Fuzzy Logic
Fuzzy Logic is a form of many-valued logic derived from fuzzy set theory. It was introduced by **Lotfi A. Zadeh** in 1965. It is used to handle uncertainty and imprecision in real-world problems.

Applications: air conditioners, washing machines, anti-lock braking systems, medical diagnosis, control systems.

### Fuzzy Set Operations

#### Union (OR)
A ∪ B: take the **maximum** membership value for each element.
- If x belongs to A with 0.5 and to B with 0.8 → union gives 0.8
- Represents "x belongs to A OR B"

#### Intersection (AND)
A ∩ B: take the **minimum** membership value.
- If x belongs to A with 0.5 and to B with 0.8 → intersection gives 0.5
- Represents "x belongs to A AND B"

#### Complement (NOT)
Ā: subtract each membership from 1.
- If x belongs to A with 0.7 → complement gives 0.3
- Represents "x does NOT belong to A"

#### Difference
A − B = A ∩ B̄ (intersection of A with complement of B)
- Elements strongly in A but weakly in B

#### Cartesian Product
A × B: creates all ordered pairs (x, y) where x ∈ A, y ∈ B.
- Membership of (x, y) = min(μ_A(x), μ_B(y))
- Creates a **fuzzy relation** — a 2D fuzzy set

#### Max-Min Composition
Combines two fuzzy relations R (on X×Y) and S (on Y×Z) into a new relation T (on X×Z).
- For each pair (x, z): find all connecting y values
- For each y: compute min(R(x,y), S(y,z)) — the weakest link in the chain
- Take the max over all y — the strongest path wins
- Used in fuzzy inference and control systems

---

## Key Concepts

| Concept | Meaning |
|---|---|
| Membership value | A number in [0,1] indicating degree of belonging |
| Fuzzy Union | max(μ_A, μ_B) for each element |
| Fuzzy Intersection | min(μ_A, μ_B) for each element |
| Complement | 1 − μ_A for each element |
| Cartesian Product | All (x,y) pairs with membership = min(μ_A(x), μ_B(y)) |
| Max-Min Composition | Combines two relations using min (chain strength) and max (best path) |

---

## Code — Line by Line

```python
def fuzzy_union(A, B):
    return {x: max(A.get(x, 0), B.get(x, 0)) for x in set(A) | set(B)}
```
Iterates over all elements in either A or B. Takes the max membership. `A.get(x, 0)` returns 0 if element x is absent from A.

```python
def fuzzy_intersection(A, B):
    return {x: min(A.get(x, 0), B.get(x, 0)) for x in set(A) | set(B)}
```
Same iteration but takes the minimum — both sets must contain the element strongly for a high result.

```python
def fuzzy_complement(A):
    return {x: 1 - A[x] for x in A}
```
Flips each membership: 0.7 becomes 0.3, 0.2 becomes 0.8.

```python
def fuzzy_difference(A, B):
    return {x: min(A.get(x, 0), 1 - B.get(x, 0)) for x in set(A) | set(B)}
```
A − B: takes min of A's membership and complement of B's. High result means "strongly in A, weakly in B".

```python
def cartesian_product(A, B):
    return {(x, y): min(A[x], B[y]) for x in A for y in B}
```
Creates every possible pair (x, y). Membership = min of both (weakest link rule).

```python
def max_min_composition(R, S):
    T = {}
    for (x, y1) in R:
        for (y2, z) in S:
            if y1 == y2:
                T[(x, z)] = max(T.get((x, z), 0), min(R[(x, y1)], S[(y2, z)]))
    return T
```
For each pair in R and S sharing a middle element (y1==y2):
- `min(R, S)` = strength of the chain x→y→z
- `max(...)` = keep the strongest chain found for (x, z)

```python
A = {'a': 0.5, 'b': 0.7, 'c': 0.2}
B = {'b': 0.6, 'c': 0.8, 'd': 0.4}
```
Sample fuzzy sets. `'b': 0.7` means element `b` belongs to A with 70% degree.

```python
R = cartesian_product(A, B)
C = {'x': 0.3, 'y': 0.9, 'z': 0.5}
S = cartesian_product(B, C)
max_min = max_min_composition(R, S)
```
Creates fuzzy relations R = A×B and S = B×C, then computes their max-min composition.
