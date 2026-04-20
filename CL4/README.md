# CL4 — Big Data Analytics & Business Intelligence
## Ubuntu Run Guide

---

## Prerequisites

```bash
sudo apt update
sudo apt install python3 python3-pip -y

pip3 install pandas matplotlib scikit-learn numpy openpyxl
```

---

## BDA P1 — Hadoop MapReduce WordCount Simulation

**File:** `bda_p1_hadoop_setup.py`

```bash
python3 bda_p1_hadoop_setup.py
```

Simulates a Hadoop MapReduce pipeline locally. Maps words to counts, shuffles, then reduces to get word frequency.

**Output:**
```
hello: 2
hadoop: 1
world: 1
```

---

## BDA P2 — Word Frequency Counter

**File:** `bda_p2_wordcount.py`

```bash
python3 bda_p2_wordcount.py
```

Counts word frequency (case-insensitive) on a fixed input string.

**Output:** `BUS=4, CAR=3, TRAIN=1`

---

## BDA P3 — MapReduce Matrix Multiplication

**File:** `bda_p3_matrix_multiply.py`

```bash
python3 bda_p3_matrix_multiply.py
```

Multiplies two sparse matrices (2×3 and 3×2) using the MapReduce pattern. Prints the resulting 2×2 matrix.

---

## BDA P4 — Student Grade Assignment (Interactive)

**File:** `bda_p4_student_grades.py`

```bash
python3 bda_p4_student_grades.py
```

Prompts for the number of students, then each student's name and marks. Uses a MapReduce pattern to assign letter grades (A/B/C/D) and prints a results table.

**Example input:**
```
Enter number of students: 3
Enter name: Alice
Enter marks: 92
Enter name: Bob
Enter marks: 74
Enter name: Carol
Enter marks: 48
```

---

## BDA P5 — Titanic Dataset Analysis

**File:** `bda_p5_titanic.py`

```bash
python3 bda_p5_titanic.py
```

Auto-downloads `Titanic.csv` from GitHub on first run. Runs two MapReduce jobs:
1. Average age of deceased passengers, grouped by gender
2. Survivor count per passenger class (1st, 2nd, 3rd)

---

## BI P6 — Data Import & Transformation

**File:** `bi_p6_import_data.py`

```bash
python3 bi_p6_import_data.py
```

Simulates Power BI's "Get Data" flow. Creates a products dataset, saves it to `products.csv`, reloads it, and filters products with price > $1.00.

**Output file:** `products.csv`

---

## BI P7 — ETL Pipeline with Visualization

**File:** `bi_p7_etl_visualization.py`

```bash
python3 bi_p7_etl_visualization.py
```

Full ETL pipeline on the Iris dataset:
- **Extract** — Load Iris dataset
- **Transform** — Handle missing values, add `sepal_area` column, map species names
- **Load** — Save to `iris_transformed.csv`
- **Visualize** — Generates histogram + scatter plot

**Output files:** `iris_transformed.csv`, `bi_p7_output.png`

> If running headless (no display), set the backend before running:
> ```bash
> MPLBACKEND=Agg python3 bi_p7_etl_visualization.py
> ```

---

## BI P8 — ETL with SQLite Database

**File:** `bi_p8_etl_database.py`

```bash
python3 bi_p8_etl_database.py
```

ETL pipeline that loads the Iris dataset, transforms it (column selection, fill missing values, add `petal_ratio`), and loads it into a local SQLite database. Then queries average petal length grouped by species.

**Output file:** `lab_database.db`

---

## BI P9 — Excel-Style Charts

**File:** `bi_p9_excel_charts.py`

```bash
python3 bi_p9_excel_charts.py
```

Generates 6 chart types (Column, Bar, Line, Pie, Scatter, Waterfall) using monthly sales/expenses/profit data.

**Output file:** `bi_p9_charts.png`

> If running headless (no display):
> ```bash
> MPLBACKEND=Agg python3 bi_p9_excel_charts.py
> ```

---

## BI P10 — Classification with Decision Tree

**File:** `bi_p10_classification.py`

```bash
python3 bi_p10_classification.py
```

Trains a Decision Tree classifier on the Iris dataset. Prints accuracy score, classification report, and confusion matrix.

---

## Quick Reference

| Program | Command |
|---|---|
| BDA P1 — Hadoop Simulation | `python3 bda_p1_hadoop_setup.py` |
| BDA P2 — Word Frequency | `python3 bda_p2_wordcount.py` |
| BDA P3 — Matrix Multiply | `python3 bda_p3_matrix_multiply.py` |
| BDA P4 — Student Grades | `python3 bda_p4_student_grades.py` |
| BDA P5 — Titanic Analysis | `python3 bda_p5_titanic.py` |
| BI P6 — Data Import | `python3 bi_p6_import_data.py` |
| BI P7 — ETL + Visualization | `python3 bi_p7_etl_visualization.py` |
| BI P8 — ETL + SQLite | `python3 bi_p8_etl_database.py` |
| BI P9 — Excel Charts | `python3 bi_p9_excel_charts.py` |
| BI P10 — Classification | `python3 bi_p10_classification.py` |

---

## Notes

- Scripts that generate charts (`bi_p7`, `bi_p9`) save `.png` files so they work on headless Ubuntu servers. Use `MPLBACKEND=Agg` if you get display errors.
- `bda_p5_titanic.py` needs internet access on first run to download `Titanic.csv`.
- `bi_p8_etl_database.py` creates `lab_database.db` in the current directory — SQLite is built into Python, no extra install needed.
