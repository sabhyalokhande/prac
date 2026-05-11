# P10 — Weather MapReduce (DC)

## What is this Practical?
Applies the **MapReduce** programming model to real weather datasets to find the hottest and coolest year. Two versions are provided — one uses a live Indian government API, the other uses NASA GISS global temperature data via a Jupyter notebook with separate mapper/reducer scripts.

---

## Theory

### Big Data and the Need for MapReduce
Modern applications generate massive amounts of data — server logs, sensor readings, social media, scientific measurements. Traditional programs that process data sequentially on one machine cannot handle this scale. MapReduce, introduced by **Google in 2004** (Jeffrey Dean & Sanjay Ghemawat), provides a framework to process data across hundreds or thousands of machines in parallel.

### MapReduce Programming Model
MapReduce breaks any data processing job into two functions that the programmer writes, and a shuffle phase that the framework handles automatically.

#### Map Phase
- Input: raw records (CSV rows, text lines, database entries)
- Output: (key, value) pairs
- Each record is processed **independently**
- Can run on many machines simultaneously
- Example: for each row, emit `(year, temperature)`

#### Shuffle & Sort Phase (automatic)
- The framework groups all values with the same key together
- Example: all temperatures for year 2020 are grouped: `2020 → [25.3, 26.1, 24.8, ...]`
- In our Unix pipeline: `sort` does this

#### Reduce Phase
- Input: (key, list_of_values) for each unique key
- Output: aggregated result per key
- Example: average all temperatures for each year
- Also runs independently per key — parallelizable

### MapReduce Data Flow
```
Input Data
    ↓
[Mapper 1]  [Mapper 2]  [Mapper 3]   ← parallel
    ↓            ↓            ↓
    └────────────┴────────────┘
         Shuffle & Sort
    ↓            ↓            ↓
[Reducer 1] [Reducer 2] [Reducer 3]  ← parallel (one per key group)
    ↓            ↓            ↓
         Final Output
```

### Why MapReduce for Weather Data?
Real weather datasets contain millions of records spanning centuries and thousands of stations. To find the hottest/coolest year:
- **Map**: extract year and temperature from each record
- **Shuffle**: group all temperatures by year
- **Reduce**: compute average per year, then find min/max

This could process a 100GB dataset across 100 machines in minutes.

### Version 1: data.gov.in API
The Indian government's Open Data platform provides free APIs for various public datasets including historical weather data. The program:
1. Fetches data over HTTP using an API key
2. Parses the CSV response
3. Applies MapReduce logic in Python classes

### Version 2: NASA GISS Dataset
NASA's Goddard Institute for Space Studies (GISS) publishes the Global Surface Temperature dataset — annual global temperature anomalies since 1880. The notebook:
1. Downloads data from NASA's servers
2. Writes `mapper.py` and `reducer.py` as separate scripts
3. Runs them through a Unix-style pipe (`cat | mapper | sort | reducer`)

### Temperature Anomaly (NASA dataset)
NASA reports **temperature anomaly** — the difference from the 1951–1980 average baseline, not absolute temperature.
- Positive value (e.g., +1.28) → warmer than baseline
- Negative value (e.g., -0.49) → cooler than baseline
- 2024: +1.28°C (warmest year on record)
- 1909: -0.49°C (coolest year in the dataset)

---

## Key Concepts

| Concept | Meaning |
|---|---|
| MapReduce | Two-phase distributed data processing: Map + Reduce |
| Map | Extract (key, value) pairs from each input record |
| Shuffle & Sort | Group all values by key before reducing |
| Reduce | Aggregate all values for each key |
| API | Application Programming Interface — fetches data from a web service |
| `defaultdict(list)` | Dictionary that auto-creates an empty list for missing keys |
| `csv.DictReader` | Parses CSV where each row becomes a Python dictionary |
| Temperature Anomaly | Deviation from a historical average baseline |

---

## Code — Line by Line

### Version 1 — p10_dc_weather_mapreduce.py

```python
self.api_key = "579b464db66ec23bdd0000016c4e9eb7c0244bcd783540de7a754501"
self.resource_id = "45787c4b-3210-4fd0-b120-63336e042370"
self.api_url = f"https://api.data.gov.in/resource/{self.resource_id}"
```
API credentials and endpoint URL for the data.gov.in Indian weather dataset.

```python
params = {"api-key": self.api_key, "format": "csv", "limit": 5000}
response = requests.get(self.api_url, params=params)
response.raise_for_status()
self.raw_data = response.text
```
Sends HTTP GET request. `raise_for_status()` raises an exception if HTTP returned an error code (4xx/5xx). Stores raw CSV text.

```python
def mapper(self, row):
    year = row["YEAR"]
    temp = float(row["ANNUAL"])
    return (year, temp)
```
**Map phase** — takes one CSV row (as a dict), extracts year and annual temperature, returns a (key, value) pair.

```python
def reducer(self, grouped_data):
    for year, temps in grouped_data.items():
        avg_temp = sum(temps) / len(temps)
        results.append((year, avg_temp))
```
**Reduce phase** — receives year → [list of temps], computes average for each year.

```python
grouped_data = defaultdict(list)
for year, temp in mapped_data:
    grouped_data[year].append(temp)
```
**Shuffle phase** — groups temperatures by year. `defaultdict(list)` automatically creates `[]` for any new year key.

```python
hottest = max(yearly_avg, key=lambda x: x[1])
coolest = min(yearly_avg, key=lambda x: x[1])
```
Finds the year with the highest and lowest average temperature using the second element (temperature) as the comparison key.

---

### Version 2 — mapper.py

```python
for line in sys.stdin:
    if line.startswith("year"):
        continue
```
Reads CSV line by line from stdin (piped from `cat weather_data.csv`). Skips the header row.

```python
    parts = line.split(",")
    year = parts[0].strip()
    temp = float(parts[1].strip())
    print(f"{year}\t{temp}")
```
Splits CSV line, extracts year and temperature, emits `year<TAB>temp` to stdout (the map output).

---

### Version 2 — reducer.py

```python
year_temps = {}
for line in sys.stdin:
    year, temp = line.strip().split("\t")
    year_temps[year].append(float(temp))
```
Reads sorted mapper output. Groups temperatures by year.

```python
avg_temps[year] = sum(temps) / len(temps)
coolest_year = min(avg_temps, key=avg_temps.get)
hottest_year = max(avg_temps, key=avg_temps.get)
```
Computes average per year. Finds hottest and coolest year.
