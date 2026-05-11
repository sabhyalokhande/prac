# CL3 — Run Guide (Ubuntu / Linux)

---

## Check if Already Installed

Run these before installing anything:

```bash
python3 --version      # should show Python 3.x.x
pip3 --version         # should show pip version
java -version          # needed only for P2 Java and P9 Java
javac -version         # needed only for P2 Java and P9 Java
```

If a command returns a version number, it is already installed — skip that install step.

---

## Prerequisites

Only install what is missing from the checks above:

```bash
sudo apt update
sudo apt install python3 python3-pip -y
pip3 install numpy scikit-learn deap requests
```

> **JDK required only for P2 Java and P9 Java.** If `java -version` showed nothing, install it:
> ```bash
> sudo apt install default-jdk -y
> ```

---

## P1 — XML-RPC Factorial Service

Open two terminals:

```bash
# Terminal 1
python3 p1_ci/server.py

# Terminal 2
python3 p1_ci/client.py
```

Enter an integer when prompted. The server returns the factorial.

---

## P2 — RMI String Concatenation (Java)

> Requires JDK — see Prerequisites above.

```bash
# Do this once in any terminal
cd p2_ci
javac *.java

# Terminal 1 — start server (already inside p2_ci)
java Server

# Terminal 2 — run client (cd into p2_ci first)
cd p2_ci
java Client
```

---

## P3 — MapReduce: Word Count

```bash
cat p3_ci/input.txt | python3 p3_ci/word_mapper.py | sort | python3 p3_ci/word_reducer.py
```

---

## P3 — MapReduce: Character Count

```bash
cat p3_ci/input.txt | python3 p3_ci/char_mapper.py | sort | python3 p3_ci/char_reducer.py
```

---

## P4 — Fuzzy Logic Operations

```bash
python3 p4_ci/fuzzy.py
```

---

## P5 — Genetic Algorithm

```bash
python3 'p5_ci/genetic_algo(A).py'
```

---

## P6 — Clonal Selection Algorithm

```bash
python3 p6_ci/clonal_selection.py
```

---

## P7 — AIRS (Artificial Immune Recognition System)

```bash
python3 p7_dc/airs.py
```

---

## P8 — DEAP Genetic Algorithm (Multiprocessing)

```bash
python3 p8_dc/deap.py
```

---

## P9 — Hotel Booking Service (Java RMI)

> Requires JDK — see Prerequisites above.

**Terminal (command line):**

```bash
# Do this once in any terminal
cd p9_dc
javac *.java

# Terminal 1 — start server (already inside p9_dc)
java HotelServer

# Terminal 2 — run client (cd into p9_dc first)
cd p9_dc
java HotelClient
```

---

**Eclipse IDE:**

1. Open Eclipse → **File → New → Java Project** → give it any name (e.g. `HotelRMI`) → Finish.
2. Open your file manager, go to the project's `src` folder, and paste all 3 files there:
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

Two versions are available inside `p10_dc/`.

---

**Version 1 — Python Script (Indian weather, data.gov.in API)**

File: `p10_dc/weather_mapreduce.py`

```bash
pip3 install requests
python3 p10_dc/weather_mapreduce.py
```

> If the API is down or returns an error, use the hardcoded fallback version in the comments at the bottom of the file.

---

**Version 2 — Jupyter Notebook + mapper/reducer (NASA GISS global temperature data)**

Files: `p10_dc/Weather_MapReduce.ipynb`, `p10_dc/mapper.py`, `p10_dc/reducer.py`, `p10_dc/weather_data.csv`

```bash
pip3 install jupyter pandas
jupyter notebook p10_dc/Weather_MapReduce.ipynb
```

In the browser that opens:
1. Click **Kernel → Restart & Run All**
2. The notebook downloads NASA data into `weather_data.csv`, then pipes it through `mapper.py` and `reducer.py` and prints the result.

> The notebook's last run cell uses a Windows `type` command internally. On Ubuntu, open the last code cell and change `type weather_data.csv` to `cat weather_data.csv` before running.

Or run it directly from terminal without Jupyter:

```bash
cat p10_dc/weather_data.csv | python3 p10_dc/mapper.py | sort | python3 p10_dc/reducer.py
```

---

## Quick Reference

| Program | Command |
|---|---|
| P1 Server | `python3 p1_ci/server.py` |
| P1 Client | `python3 p1_ci/client.py` |
| P2 Java | `cd p2_ci && javac *.java` then `java Server` / `java Client` |
| P3 Word Count | `cat p3_ci/input.txt \| python3 p3_ci/word_mapper.py \| sort \| python3 p3_ci/word_reducer.py` |
| P3 Char Count | `cat p3_ci/input.txt \| python3 p3_ci/char_mapper.py \| sort \| python3 p3_ci/char_reducer.py` |
| P4 Fuzzy | `python3 p4_ci/fuzzy.py` |
| P5 Genetic | `python3 'p5_ci/genetic_algo(A).py'` |
| P6 Clonal Selection | `python3 p6_ci/clonal_selection.py` |
| P7 AIRS | `python3 p7_dc/airs.py` |
| P8 DEAP | `python3 p8_dc/deap.py` |
| P9 Hotel Java | `cd p9_dc && javac *.java` then `java HotelServer` / `java HotelClient` |
| P10 Script | `python3 p10_dc/weather_mapreduce.py` |
| P10 Notebook | `jupyter notebook p10_dc/Weather_MapReduce.ipynb` |
