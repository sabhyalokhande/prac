# CL3 — Run Guide (Windows)

---

## Check if Already Installed

Open **Command Prompt** or **PowerShell** and run:

```cmd
python --version
pip --version
java -version
javac -version
```

If a command returns a version number, it is already installed — skip that install step.

---

## Prerequisites

Only install what is missing from the checks above:

1. **Python 3** — Download from [python.org](https://www.python.org/downloads/). During install, check **"Add Python to PATH"**.
2. Open **Command Prompt** or **PowerShell** and install Python packages:

```cmd
pip install numpy scikit-learn deap requests
```

> **JDK required only for P2 Java and P9 Java.** If `java -version` showed nothing, download JDK from [adoptium.net](https://adoptium.net/). During install, check **"Set JAVA_HOME variable"**.

---

## P1 — XML-RPC Factorial Service

Open two Command Prompt windows:

```cmd
:: Window 1
python p1_ci\server.py

:: Window 2
python p1_ci\client.py
```

Enter an integer when prompted. The server returns the factorial.

---

## P2 — RMI String Concatenation (Java)

> Requires JDK — see Prerequisites above.

```cmd
:: Do this once in any window
cd p2_ci
javac *.java

:: Window 1 — start server (already inside p2_ci)
java Server

:: Window 2 — run client (cd into p2_ci first)
cd p2_ci
java Client
```

---

## P3 — MapReduce: Word Count

Use PowerShell:

```powershell
Get-Content p3_ci\input.txt | python p3_ci\word_mapper.py | Sort-Object | python p3_ci\word_reducer.py
```

---

## P3 — MapReduce: Character Count

```powershell
Get-Content p3_ci\input.txt | python p3_ci\char_mapper.py | Sort-Object | python p3_ci\char_reducer.py
```

---

## P4 — Fuzzy Logic Operations

```cmd
python p4_ci\fuzzy.py
```

---

## P5 — Genetic Algorithm

```cmd
python "p5_ci\genetic_algo(A).py"
```

---

## P6 — Clonal Selection Algorithm

```cmd
python p6_ci\clonal_selection.py
```

---

## P7 — AIRS (Artificial Immune Recognition System)

```cmd
python p7_dc\airs.py
```

---

## P8 — DEAP Genetic Algorithm (Multiprocessing)

```cmd
python p8_dc\deap.py
```

---

## P9 — Hotel Booking Service (Java RMI)

> Requires JDK — see Prerequisites above.

**Command Prompt:**

```cmd
:: Do this once in any window
cd p9_dc
javac *.java

:: Window 1 — start server (already inside p9_dc)
java HotelServer

:: Window 2 — run client (cd into p9_dc first)
cd p9_dc
java HotelClient
```

---

**Eclipse IDE:**

1. Open Eclipse → **File → New → Java Project** → give it any name (e.g. `HotelRMI`) → Finish.
2. Open File Explorer, go to the project's `src` folder, and paste all 3 files there:
   `HotelInterface.java`, `HotelServer.java`, `HotelClient.java`
3. Back in Eclipse, right-click the project → **Refresh** — all 3 files will appear and auto-compile.
4. Right-click `HotelServer.java` → **Run As → Java Application** — the Console tab will show `Hotel Server is running...`
5. Right-click `HotelClient.java` → **Run As → Java Application** — a second Console tab opens with the booking menu.
6. Use the dropdown arrow on the Console tab to switch between server and client output.

> Do not stop the server before finishing with the client.

---

**BlueJ IDE:**

1. Open BlueJ → **Project → New Project** → give it any name → OK.
2. **Edit → Add Class From File** → select `HotelInterface.java` → repeat for `HotelServer.java` and `HotelClient.java`.
3. Click **Compile** (the button at the top) — all boxes should turn white (no stripes).
4. Right-click the `HotelServer` box → **void main(String[] args)** → OK → a BlueJ Terminal opens showing `Hotel Server is running...`
5. Right-click the `HotelClient` box → **void main(String[] args)** → OK → another BlueJ Terminal opens with the booking menu.

> Keep the server terminal open while using the client.

---

## P10 — Weather MapReduce

Two versions are available inside `p10_dc\`.

---

**Version 1 — Python Script (Indian weather, data.gov.in API)**

File: `p10_dc\weather_mapreduce.py`

```cmd
pip install requests
python p10_dc\weather_mapreduce.py
```

> If the API is down or returns an error, use the hardcoded fallback version in the comments at the bottom of the file.

---

**Version 2 — Jupyter Notebook + mapper/reducer (NASA GISS global temperature data)**

Files: `p10_dc\Weather_MapReduce.ipynb`, `p10_dc\mapper.py`, `p10_dc\reducer.py`, `p10_dc\weather_data.csv`

```cmd
pip install jupyter pandas
jupyter notebook p10_dc\Weather_MapReduce.ipynb
```

In the browser that opens:
1. Click **Kernel → Restart & Run All**
2. The notebook downloads NASA data into `weather_data.csv`, then pipes it through `mapper.py` and `reducer.py` and prints the result.

Or run it directly from Command Prompt without Jupyter:

```cmd
type p10_dc\weather_data.csv | python p10_dc\mapper.py | sort | python p10_dc\reducer.py
```

---

## Quick Reference

| Program | Command |
|---|---|
| P1 Server | `python p1_ci\server.py` |
| P1 Client | `python p1_ci\client.py` |
| P2 Java | `cd p2_ci && javac *.java` then `java Server` / `java Client` |
| P3 Word Count | `Get-Content p3_ci\input.txt \| python p3_ci\word_mapper.py \| Sort-Object \| python p3_ci\word_reducer.py` |
| P3 Char Count | `Get-Content p3_ci\input.txt \| python p3_ci\char_mapper.py \| Sort-Object \| python p3_ci\char_reducer.py` |
| P4 Fuzzy | `python p4_ci\fuzzy.py` |
| P5 Genetic | `python "p5_ci\genetic_algo(A).py"` |
| P6 Clonal Selection | `python p6_ci\clonal_selection.py` |
| P7 AIRS | `python p7_dc\airs.py` |
| P8 DEAP | `python p8_dc\deap.py` |
| P9 Hotel Java | `cd p9_dc && javac *.java` then `java HotelServer` / `java HotelClient` |
| P10 Script | `python p10_dc\weather_mapreduce.py` |
| P10 Notebook | `jupyter notebook p10_dc\Weather_MapReduce.ipynb` |

---

## Tips

- If `python` is not recognized, try `py` instead (Windows Python Launcher).
- If `javac` is not recognized, ensure the JDK `bin` folder is added to your **PATH** environment variable.
