# P3 — MapReduce: Word Count & Character Count

## What is this Practical?
Implements the **MapReduce** programming model using Unix pipes. Input text is processed in two stages — Map and Reduce — simulating how Hadoop processes big data across many machines, but using simple Python scripts and the shell.

---

## Theory

### Why MapReduce?
Traditional programs process data sequentially on one machine. When data is too large to fit on one machine (terabytes/petabytes), you need to distribute the work across many machines. MapReduce is a programming model designed for this. It was popularized by Google's 2004 research paper and later implemented as **Apache Hadoop**.

### The MapReduce Model
MapReduce breaks any large data processing job into three phases:

#### 1. Map Phase
- Input: raw records (lines of text, rows of a database, etc.)
- Task: process each record independently and emit **(key, value)** pairs
- Example: for each word in a line, emit `(word, 1)`
- Each mapper runs independently — no communication between mappers
- This makes it trivially parallelizable across thousands of machines

#### 2. Shuffle & Sort Phase
- Automatically done by the framework (or by `sort` in our pipeline)
- Groups all values with the same key together
- Example: `apple 1`, `apple 1`, `banana 1` → `apple [1,1]`, `banana [1]`
- Essential step — ensures the reducer sees ALL values for a key at once

#### 3. Reduce Phase
- Input: a key and a list of all values for that key
- Task: aggregate the values into a single result
- Example: `apple [1, 1]` → `apple 2`
- Reducers also run independently per key

### How Our Pipeline Simulates MapReduce
```
cat input.txt          →  provides raw input line by line
| python3 mapper.py    →  Map phase: emits (word, 1) pairs
| sort                 →  Shuffle & Sort: groups same words together
| python3 reducer.py   →  Reduce phase: sums counts per word
```
The Unix pipe (`|`) connects `stdout` of one program to `stdin` of the next — exactly how data flows in real MapReduce.

### Tab-Separated Output (`\t`)
Mappers use a tab character to separate key from value: `word\t1`. This is a convention in Hadoop streaming — tab separates key and value in intermediate output.

### Word Count vs Character Count
- **Word Count**: splits each line into words, emits `(word, 1)` for each
- **Character Count**: iterates over each character, emits `(char, 1)` for each non-space character

Both use the exact same reducer logic — they only differ in what the mapper emits.

### Real-World Usage
MapReduce is used for:
- Web indexing (Google processes billions of pages)
- Log analysis (find errors across millions of server log files)
- Data mining and analytics at massive scale
- Training machine learning models on distributed data

---

## Key Concepts

| Concept | Meaning |
|---|---|
| Map | Transform each input record into (key, value) pairs |
| Shuffle & Sort | Group all values with the same key together |
| Reduce | Aggregate values per key into a final result |
| `sys.stdin` | Reads input piped from previous command |
| `\t` | Tab character used as key-value separator |
| Unix Pipe `\|` | Connects output of one program to input of the next |
| `sort` | Shell command that sorts lines alphabetically — groups same keys |

---

## Code — Line by Line

### word_mapper.py

```python
import sys
```
Imports `sys` to read from standard input (data piped in from `cat input.txt`).

```python
for line in sys.stdin:
    line = line.strip()
```
Reads one line at a time. `.strip()` removes the trailing newline character.

```python
    words = line.split()
    for word in words:
        print(f"{word.lower()}\t1")
```
Splits the line into words. For each word, prints `word<TAB>1` — the mapper output that represents "I saw this word once". Lowercased so `The` and `the` are treated as the same word.

---

### word_reducer.py

```python
current_word = None
current_count = 0
```
State variables — track which word is being summed and its running total. Works because input is **sorted**, so all occurrences of a word arrive consecutively.

```python
for line in sys.stdin:
    word, count = line.strip().split('\t')
    count = int(count)
```
Reads each `word<TAB>1` line from the sorted mapper output. Splits on tab to get word and count.

```python
    if current_word == word:
        current_count += count
    else:
        if current_word:
            print(f"{current_word}\t{current_count}")
        current_word = word
        current_count = count
```
If the same word continues, accumulate. When a new word is seen, print the previous word's total and start fresh.

```python
if current_word:
    print(f"{current_word}\t{current_count}")
```
The last word is never printed inside the loop (no "new word" to trigger it), so it must be printed after the loop ends.

---

### char_mapper.py

```python
for char in line:
    if char.strip() != "":
        print(f"{char}\t1")
```
Iterates over every character. Skips spaces (`char.strip() != ""`). Emits `char<TAB>1` for every non-space character.

---

### char_reducer.py
Identical logic to `word_reducer.py` — just uses `current_char` instead of `current_word`. Groups and sums counts for each individual character.
