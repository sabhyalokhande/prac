# CL3 — Computational Intelligence & Distributed Computing
## Ubuntu Run Guide

---

## Prerequisites

```bash
sudo apt update
sudo apt install python3 python3-pip default-jdk -y

pip3 install numpy scikit-learn deap requests
```

---

## P1 — XML-RPC Factorial Service

**Files:** `ci_p1_server.py`, `ci_p1_client.py`

Open two terminals:

```bash
# Terminal 1 — start server
python3 ci_p1_server.py

# Terminal 2 — run client
python3 ci_p1_client.py
```

Enter an integer when prompted. The server calculates and returns the factorial.

---

## P2 — XML-RPC String Concatenation (Python)

**Files:** `ci_p2_server.py`, `ci_p2_client.py`

Open two terminals:

```bash
# Terminal 1 — start server
python3 ci_p2_server.py

# Terminal 2 — run client
python3 ci_p2_client.py
```

Enter two strings when prompted. The server concatenates and returns them.

---

## P2 — RMI String Concatenation (Java)

**Files:** `ci_p2/StringRemote.java`, `ci_p2/StringRemoteImpl.java`, `ci_p2/Server.java`, `ci_p2/Client.java`

```bash
cd ci_p2

# Compile all Java files
javac *.java
```

Open two terminals:

```bash
# Terminal 1 — start RMI server
java Server

# Terminal 2 — run client
java Client
```

---

## P3 — MapReduce: Word Count

**Files:** `ci_p3_word_mapper.py`, `ci_p3_word_reducer.py`

Requires `input.txt` in the same directory.

```bash
cat input.txt | python3 ci_p3_word_mapper.py | sort | python3 ci_p3_word_reducer.py
```

---

## P3 — MapReduce: Character Count

**Files:** `ci_p3_char_mapper.py`, `ci_p3_char_reducer.py`

```bash
cat input.txt | python3 ci_p3_char_mapper.py | sort | python3 ci_p3_char_reducer.py
```

---

## P4 — Fuzzy Logic Operations

**File:** `ci_p4_fuzzy.py`

```bash
python3 ci_p4_fuzzy.py
```

Outputs union, intersection, complement, difference, Cartesian product, and max-min composition on sample fuzzy sets.

---

## P5 — Genetic Algorithm (Neural Network Hyperparameter Tuning)

**File:** `ci_p5_genetic_algo.py`

```bash
python3 ci_p5_genetic_algo.py
```

Runs 10 generations and prints the best MSE and hyperparameters (population size, crossover rate, mutation rate) found.

---

## P6 — Clonal Selection Algorithm

**File:** `ci_p6_clonal_selection.py`

```bash
python3 ci_p6_clonal_selection.py
```

Minimizes x² using an artificial immune system. Prints the best solution at each of 20 iterations.

---

## P7 — AIRS (Artificial Immune Recognition System)

**File:** `dc_p7_airs.py`

```bash
python3 dc_p7_airs.py
```

Trains detectors on synthetic health/damage data and prints classification accuracy.

---

## P8 — DEAP Genetic Algorithm (Multiprocessing)

**File:** `dc_p8_deap.py`

```bash
pip3 install deap
python3 dc_p8_deap.py
```

Minimizes x₁² + x₂² + x₃² over 20 generations using parallel fitness evaluation. Prints best fitness and individual per generation.

---

## P9 — Hotel Booking Service (Python XML-RPC)

**Files:** `dc_p9_hotel_server.py`, `dc_p9_hotel_client.py`

Open two terminals:

```bash
# Terminal 1 — start server
python3 dc_p9_hotel_server.py

# Terminal 2 — run client
python3 dc_p9_hotel_client.py
```

Client menu: `1` = Book Room, `2` = Cancel Booking, `3` = Exit.

---

## P9 — Hotel Booking Service (Java RMI)

**Files:** `dc_p9/HotelInterface.java`, `dc_p9/HotelServer.java`, `dc_p9/HotelClient.java`

```bash
cd dc_p9
javac *.java
```

Open two terminals:

```bash
# Terminal 1 — start RMI server
java HotelServer

# Terminal 2 — run client
java HotelClient
```

---

## P10 — Weather MapReduce (API)

**File:** `ci_p10_weather_mapreduce.py`

```bash
pip3 install requests
python3 ci_p10_weather_mapreduce.py
```

Fetches Indian weather data from data.gov.in, computes yearly average temperatures, and reports the hottest and coolest year.

---

## Quick Reference

| Program | Command |
|---|---|
| P1 Server | `python3 ci_p1_server.py` |
| P1 Client | `python3 ci_p1_client.py` |
| P2 Server (Python) | `python3 ci_p2_server.py` |
| P2 Client (Python) | `python3 ci_p2_client.py` |
| P2 Java | `cd ci_p2 && javac *.java && java Server` / `java Client` |
| P3 Word Count | `cat input.txt \| python3 ci_p3_word_mapper.py \| sort \| python3 ci_p3_word_reducer.py` |
| P3 Char Count | `cat input.txt \| python3 ci_p3_char_mapper.py \| sort \| python3 ci_p3_char_reducer.py` |
| P4 Fuzzy | `python3 ci_p4_fuzzy.py` |
| P5 Genetic Algo | `python3 ci_p5_genetic_algo.py` |
| P6 Clonal Selection | `python3 ci_p6_clonal_selection.py` |
| P7 AIRS | `python3 dc_p7_airs.py` |
| P8 DEAP | `python3 dc_p8_deap.py` |
| P9 Hotel Server (Python) | `python3 dc_p9_hotel_server.py` |
| P9 Hotel Client (Python) | `python3 dc_p9_hotel_client.py` |
| P9 Hotel Java | `cd dc_p9 && javac *.java && java HotelServer` / `java HotelClient` |
| P10 Weather | `python3 ci_p10_weather_mapreduce.py` |
