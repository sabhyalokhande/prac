# Lab Practical 9 — Data Analysis and Visualization using Advanced Excel

**Aim:** Data Analysis and Visualization using Advanced Excel.

---

## STEP 1: Open Excel & Enter Data

1. Open **Microsoft Excel**
2. Enter the following data starting from cell **A1**:

| Month | Television | Laptop | Mobile Phones |
|-------|-----------|--------|---------------|
| Jan   | 145       | 335    | 82            |
| Feb   | 145       | 362    | 126           |
| Mar   | 105       | 311    | 95            |
| Apr   | 171       | 259    | 93            |
| May   | 178       | 277    | 107           |
| Jun   | 167       | 292    | 145           |
| Jul   | 200       | 385    | 77            |
| Aug   | 181       | 388    | 78            |
| Sep   | 152       | 291    | 83            |
| Oct   | 143       | 345    | 102           |
| Nov   | 114       | 399    | 99            |
| Dec   | 109       | 250    | 101           |
| Total | 1810      | 3894   | 1188          |

3. In the **Total** row, use `=SUM()` to sum each column:
   - `=SUM(B2:B13)` for Television
   - `=SUM(C2:C13)` for Laptop
   - `=SUM(D2:D13)` for Mobile Phones

---

## STEP 2: Create COLUMN CHART

1. Select the data range **A1:D13** (excluding Total row)
2. Go to **Insert** tab → **Charts** group → click **Column Chart** icon
3. Select **Clustered Column** (first option)
4. A column chart appears showing all three products by month

---

## STEP 3: Create BAR CHART

1. Select the data range **A1:D13**
2. Go to **Insert** tab → **Charts** group → click **Bar Chart** icon
3. Select **Clustered Bar** (first option)
4. A horizontal bar chart appears comparing products across months

---

## STEP 4: Create LINE CHART

1. Select the data range **A1:D13**
2. Go to **Insert** tab → **Charts** group → click **Line Chart** icon
3. Select **Line with Markers** (fourth option)
4. A line chart appears showing trends for each product across months

---

## STEP 5: Create PIE CHART

1. Select the **three total values** vertically — cells **B14**, **C14**, **D14**:
   - B14 = 1810 (Television)
   - C14 = 3894 (Laptop)
   - D14 = 1188 (Mobile Phones)
2. Go to **Insert** → **Chart**
3. In the Chart Editor panel (right side), change the **Chart type** to **Pie chart**
4. Google Sheets automatically uses the column headers (Television, Laptop, Mobile Phones) as slice labels
5. A pie chart appears with 3 slices showing proportion of total annual sales per product

---

## STEP 6: Create SCATTER PLOT

1. Select the data range **A1:D13**
2. Go to **Insert** tab → **Charts** group → click **Scatter (X,Y)** icon
3. Select **Scatter with Straight Lines and Markers**
4. A scatter plot appears with data points connected by lines

---

## STEP 7: Create WATERFALL CHART

1. Select the data range **A1:D13** (or just one product column, e.g., **A1:B13**)
2. Go to **Insert** tab → **Charts** group → click **Insert Waterfall or Stock Chart** icon
3. Select **Waterfall**
4. A waterfall chart appears showing cumulative values month by month

> **Note:** For Waterfall chart, if you want to show the Total as a summary bar:
> - Right-click the **Total** bar in the chart → **Format Data Point** → check **Set as total**

---

## STEP 8: Customize Chart

### Edit Chart Title

1. Click on the chart to select it
2. In the **Chart Design** ribbon → click **Chart Title** dropdown
3. Select **Above Chart** → a text box "Chart Title" appears on the chart
4. Click on the title text box → type `Electronic Store Sales 2022` → press **Enter**

   Alternatively:
   - Right-click the chart → **Edit Chart Title** → type `Electronic Store Sales 2022` → click **OK**

---

### Display Data Labels

1. Click on the chart to select it
2. In the **Chart Design** ribbon → click **Data Labels** dropdown
3. Choose a position:
   - **None** — hides all labels
   - **Center** — labels centered on bars
   - **Inside End** — labels inside the top of bars
   - **Inside Base** — labels at the bottom inside bars
   - **Outside End** — labels above/outside the bars (most common for column charts)
4. Select **Outside End** to display values on top of each bar

---

## Result

Advanced Excel charts created for Electronic Store Sales 2022 data:
- **Column Chart** — comparison of products by month (vertical bars)
- **Bar Chart** — horizontal comparison of products by month
- **Line Chart** — trend lines showing sales over 12 months
- **Pie Chart** — proportion of total annual sales per product
- **Scatter Plot** — data point distribution across months
- **Waterfall Chart** — cumulative sales progression month by month
- **Customization** — chart title set to "Electronic Store Sales 2022" and data labels added
