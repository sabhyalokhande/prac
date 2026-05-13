# CL4 — Index of All Practicals

**Subject:** Computer Laboratory IV (Big Data Analytics + Business Intelligence)  
**Institute:** Dr. D.Y. Patil Institute of Engineering, Management and Research, Akurdi, Pune  
**Class:** B.E. (AI & DS) | Roll No: BEAD-64

---

## Quick Navigation

| PS No. | Problem Statement | Folder | Type |
|--------|------------------|--------|------|
| [PS 1](#ps-1--hadoop-setup--configuration) | Set up and Configuration Hadoop | `1/` | BDA |
| [PS 2](#ps-2--wordcount-mapreduce) | MapReduce — Word Frequency Count | `2/` | BDA |
| [PS 3](#ps-3--matrix-multiplication-mapreduce) | MapReduce — Matrix Multiplication | `3/` | BDA |
| [PS 4](#ps-4--student-grades-mapreduce) | MapReduce — Student Grades | `4/` | BDA |
| [PS 5](#ps-5--titanic-analysis-mapreduce) | MapReduce — Titanic Ship Analysis | `5/` | BDA |
| [PS 6](#ps-6--import-data-from-sources-power-bi) | Import Data from Sources (Power BI) | `6/` | BI |
| [PS 7](#ps-7--etl--data-visualization-python) | ETL + Data Visualization (Python) | `7/` | BI |
| [PS 8](#ps-8--etl-process-power-bi) | ETL Process — Power BI | `8/` | BI |
| [PS 9](#ps-9--advanced-excel-charts) | Data Analysis using Advanced Excel | `9/` | BI |
| [PS 10](#ps-10--data-classification-logistic-regression) | Data Classification Algorithm | `10/` | BI |

---

## PS 1 — Hadoop Setup & Configuration

**Problem Statement:** Set up and Configuration Hadoop Using CloudEra / Google Cloud BigQuery. Databricks Lakehouse Platform. Snowflake. Amazon Redshift.

**Folder:** `CL4/1/`

| File | Description |
|------|-------------|
| `Lab1_README.md` | Step-by-step Hadoop 3.3.6 setup — Windows (7 phases: Java, Hadoop+winutils, 5 XML configs, format, start/stop, WordCount) + Ubuntu (10 phases: Java, bashrc, download, XML configs, SSH, dirs, format, start/stop, WordCount) + troubleshooting tables |
| `Hadoop_Setup_Windows_and_Ubuntu.pdf` | Complete Hadoop 3.3.6 setup guide for Windows and Ubuntu — Java install, XML config, winutils, SSH, start/stop commands, troubleshooting |
| `Lab_1_Hadoop_Setup_CloudEra_BigQuery_Databricks_Snowflake_Redshift.pdf` | Official lab assignment sheet for PS 1 |

**Also see:** [`CL4/Hadoop_Guide.md`](Hadoop_Guide.md) — Full Hadoop theory, architecture, advantages, disadvantages, commands, and complete setup guide for both Windows and Ubuntu.

---

## PS 2 — WordCount MapReduce

**Problem Statement:** Develop a MapReduce program to calculate the frequency of a given word in a given file.

**Folder:** `CL4/2/`

| File | Description |
|------|-------------|
| `Lab2_README.md` | Step-by-step guide — WordCount.java full code (MyMapper splits by comma + toUpperCase, MyReducer sums), compile command, JAR creation, HDFS upload, run command, expected output |
| `BDA_CLIV_2.pdf` | Sabhya's submission PDF for PS 2 |
| `Lab_2_MapReduce_Word_Frequency.pdf` | Official lab assignment sheet for PS 2 |

**Input:** `wordcount.txt` — `Bus, Car, bus, car, train, car, bus, BUS`  
**Output:** `BUS=4, CAR=3, TRAIN=1`

---

## PS 3 — Matrix Multiplication MapReduce

**Problem Statement:** Implement Matrix Multiplication using MapReduce.

**Folder:** `CL4/3/`

| File | Description |
|------|-------------|
| `Lab3_README.md` | Step-by-step guide — Multiply.java (MatrixMapper + MatrixReducer), input format (M,row,col,val + N,row,col,val), compile, JAR, HDFS upload, run, expected output |
| `BDA_CLIV_3.pdf` | Sabhya's submission PDF for PS 3 |
| `Lab_3_Matrix_Multiplication_MapReduce.pdf` | Official lab assignment sheet for PS 3 |

**Input:** Matrix M (2×3) and Matrix N (3×2) combined in `input.txt`  
**Output:** `0,0=58 | 0,1=64 | 1,0=139 | 1,1=154`

---

## PS 4 — Student Grades MapReduce

**Problem Statement:** Develop a MapReduce program to find the grades of students.

**Folder:** `CL4/4/`

| File | Description |
|------|-------------|
| `Lab4_README.md` | Step-by-step guide — 3 Java files (GradeMapper, GradeReducer, GradeDriver), grade scale (A/B/C/D), compile, JAR, HDFS upload, run, expected output |
| `BDA_CLIV_4.pdf` | Sabhya's submission PDF for PS 4 |
| `Lab_4_MapReduce_Student_Grades.pdf` | Official lab assignment sheet for PS 4 |

**Input:** `student.txt` — `Alice 95, Bob 80, Charlie 60, David 45, Eve 30`  
**Output:** `Alice=A, Bob=B, Charlie=C, David=D, Eve=D`

**Grade Scale:** ≥90→A | ≥75→B | ≥50→C | <50→D

---

## PS 5 — Titanic Analysis MapReduce

**Problem Statement:** Develop a MapReduce program to analyze Titanic ship data — find average age of dead males and count of dead females per class.

**Folder:** `CL4/5/`

| File | Description |
|------|-------------|
| `Lab5_README.md` | Step-by-step guide — Part A: DeadMaleMapper/Reducer/Driver (avg age of dead males), Part B: FemaleClassMapper/Reducer/Driver (dead females per class), two JARs, two HDFS outputs |
| `BDA_CLIV_5.pdf` | Sabhya's submission PDF for PS 5 |
| `Lab_5_MapReduce_Titanic_Analysis.pdf` | Official lab assignment sheet for PS 5 |

**Dataset:** `Titanic.csv` (download from GitHub datasciencedojo)  
**Output Part A:** `Dead_Male = 31` (avg age)  
**Output Part B:** `Class_1=3 | Class_2=6 | Class_3=72`

---

## PS 6 — Import Data from Sources (Power BI)

**Problem Statement:** Import Data from different Sources such as Excel, SQL Server, Oracle etc. and load in targeted system.

**Folder:** `CL4/6/`

| File | Description |
|------|-------------|
| `Lab6_README.md` | Steps for Power BI — Part A: Import from Excel (Superstore_Sample.xlsx via Get Data), Part B: Import from OData Feed (Northwind URL, select Orders table) |
| `Superstore_Sample.xlsx` | Sample Excel dataset used in Part A |
| `Practical1_Import_Data_Sources.pdf` | Sabhya's submission PDF for PS 6 |
| `Practical_06.pdf` | Official lab assignment sheet for PS 6 |

**Tool:** Power BI Desktop  
**Sources:** Excel (.xlsx) and OData Feed (Northwind)

---

## PS 7 — ETL + Data Visualization (Python)

**Problem Statement:** Data Visualization from Extraction Transformation and Loading (ETL) Process.

**Folder:** `CL4/7/`

### Code 1 — Superstore (Recommended per lab manual)
**Subfolder:** `code 1 - superstore/`

| File | Description |
|------|-------------|
| `pract8.ipynb` | Jupyter notebook — Extract (Superstore.csv, 9994×21), Transform (dropna, select 5 cols, drop_duplicates → 7729×5), Load (to CSV), Visualize (bar chart + line chart by Category) |
| `Lab7_README.md` | Step-by-step guide for Superstore ETL code |
| `Superstore.csv` | Dataset used in the notebook |
| `Practical2_Data_Visualization_ETL.pdf` | Sabhya's submission PDF for PS 7 |

### Code 2 — Iris (Matches Sabhya's PDF submission)
**Subfolder:** `code 2 - iris/`

| File | Description |
|------|-------------|
| `Lab7_Iris_README.md` | Step-by-step guide — Extract (Iris.csv), Transform (isnull check, PetalArea column, species rename), Load (iris_cleaned.csv), Visualize (histogram + scatter plot) |
| `iris.csv` | Iris dataset |

**Tool:** Jupyter Notebook (Python — pandas, matplotlib)

---

## PS 8 — ETL Process (Power BI)

**Problem Statement:** Perform the Extraction Transformation and Loading (ETL) process to construct the database in the SQL server / Power BI.

**Folder:** `CL4/8/`

| File | Description |
|------|-------------|
| `Lab8_README.md` | Step-by-step guide — Extract (Get Data → Excel → Superstore Sample.xlsx), Transform (remove columns, handle missing values, change data types, add Profit Margin custom column), Load (Close & Apply), Database Construction (Data view + Model view) |
| `Superstore_Sample.xlsx` | Dataset used for ETL in Power BI |
| `Practical3_ETL_PowerBI.pdf` | Sabhya's submission PDF for PS 8 |
| `Practical_08.pdf` | Official lab assignment sheet for PS 8 |

**Tool:** Power BI Desktop (Power Query Editor)  
**Custom Column Formula:** `= [Profit] / [Sales] * 100` (Profit Margin)

---

## PS 9 — Advanced Excel Charts

**Problem Statement:** Data Analysis and Visualization using Advanced Excel.

**Folder:** `CL4/9/`

| File | Description |
|------|-------------|
| `Lab9_README.md` | Step-by-step guide — Enter sales data (Month/TV/Laptop/Mobile, 12 months), create Column chart, Bar chart, Line chart, Pie chart (select B14:D14 totals → Insert → Chart → Pie), Scatter plot (select B1:D13, no Month column), Waterfall chart, Customize (title + data labels) |
| `Sales_Data.xlsx` | Electronic Store Sales 2022 dataset |
| `9th-visualization-excel.xlsx` | Excel file with charts already created |
| `Practical_09.pdf` | Official lab assignment sheet for PS 9 |

**Tool:** LibreOffice Calc / Microsoft Excel / Google Sheets  
**Charts created:** Column, Bar, Line, Pie, Scatter, Waterfall

---

## PS 10 — Data Classification (Logistic Regression)

**Problem Statement:** Perform the data classification algorithm using any Classification algorithm.

**Folder:** `CL4/10/`

### Code 1 — Titanic (Recommended per lab manual)
**Subfolder:** `code 1 - titanic/`

| File | Description |
|------|-------------|
| `pract10.ipynb` | Jupyter notebook — Logistic Regression on Titanic data (seaborn), feature selection, fillna, get_dummies, train_test_split (80/20), accuracy_score, classification_report, confusion_matrix, 2 countplot visualizations |

### Code 2 — Iris (Matches Sabhya's PDF submission)
**Subfolder:** `code 2 - iris/`

| File | Description |
|------|-------------|
| `Lab10_README.md` | Step-by-step guide — Import libraries, load Iris.csv, prepare X/y, LabelEncoder, train_test_split (70/30), LogisticRegression(max_iter=200), predict, ConfusionMatrixDisplay |
| `iris.csv` | Iris dataset (150 rows, 5 columns) |

**Tool:** Jupyter Notebook (Python — pandas, sklearn, matplotlib)  
**Algorithm:** Logistic Regression  
**Output:** Confusion matrix (12/17/16 on diagonal = 100% accuracy)

---

## Root Level Files

| File | Description |
|------|-------------|
| `Hadoop_Guide.md` | Complete Hadoop guide — theory, architecture, advantages, disadvantages, HDFS/YARN concepts, all commands, Windows + Ubuntu setup |
| `INDEX.md` | This file — index of all practicals and folder contents |
| `CL4-labmanual-full.pdf` | Full official lab manual for CL4 |
| `outputs.pdf` | Sample outputs PDF |
