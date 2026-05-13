# Lab Practical 8 — ETL Process in Power BI

**Aim:** Perform the Extraction, Transformation and Loading (ETL) process to construct the database in Power BI.

---

## How to Open Power BI Desktop

1. Press **Windows** key → search **Power BI Desktop** → click to open
2. Sign in with your Microsoft account (optional for desktop use)
3. The main window opens with **Home**, **Insert**, **Modeling**, **View** ribbons at the top

---

## STEP 1: Extraction (Load Data)

1. From the **Home** ribbon, click **Get Data** → **Excel workbook**
2. In the Open File dialog, browse and select **Superstore Sample.xlsx**
3. In the **Navigator** pane, select the **Superstore** table
4. Click **Transform Data** to open Power Query Editor

The data loads with columns:
- Row ID, Order ID, Order Date, Ship Date, Ship Mode
- Customer ID, Customer Name, Segment, Country, City, State
- Postal Code, Region, Product ID, Category, Sub-Category
- Product Name, Sales, Quantity, Discount, Profit

---

## STEP 2: Transformation

### (A) Remove Unnecessary Columns

1. In Power Query Editor, go to **Home** → **Choose Columns**
2. In the **Choose Columns** dialog, keep only the required columns:
   - ✅ Category
   - ✅ Sub-Category
   - ✅ Sales
   - ✅ Quantity
   - ✅ Profit
3. Uncheck all other columns → Click **OK**

---

### (B) Handle Missing Values

1. In Power Query Editor, go to **Home** → **Remove Rows**
2. Select **Remove Blank Rows** — removes all blank rows from the table
3. Alternatively, right-click any column → **Remove Errors** to remove error rows

---

### (C) Change the Data Type

1. Click on the column header (e.g., **Sales**)
2. In the **Transform** ribbon → **Data Type** dropdown
3. Set appropriate types:
   - Sales → **Decimal Number**
   - Quantity → **Whole Number**
   - Profit → **Decimal Number**
   - Category, Sub-Category → **Text**

---

### (D) Create a New Column (Profit Margin)

1. Go to **Add Column** ribbon → **Custom Column**
2. In the **Custom Column** dialog:
   - **New column name:** `Profit Margin`
   - **Custom column formula:**
     ```
     = [Profit] / [Sales] * 100
     ```
3. Click **OK** — new `Profit Margin` column is added to the table

---

## STEP 3: Loading

1. In Power Query Editor, click **Close & Apply** (top-left)
2. This closes the editor and applies all transformations
3. The cleaned data with 6 columns (Category, Sub-Category, Sales, Quantity, Profit, Profit Margin) is now loaded into Power BI

---

## STEP 4: Database Construction

1. Go to **Data view** (table icon on the left sidebar)
2. The **Superstore** table is now visible with all transformed columns:
   - Category, Sub-Category, Sales, Quantity, Profit, Profit Margin
3. Go to **Model view** to see table relationships
4. In the **Fields** pane (right side), you can see all columns listed under the Superstore table

The database is now constructed and ready for reporting and visualization in Power BI.

---

## Result

ETL process completed in Power BI:
- **Extracted** — Superstore Excel data loaded via Get Data
- **Transformed** — removed unnecessary columns, handled missing values, changed data types, added Profit Margin column
- **Loaded** — cleaned data applied and database constructed in Power BI Desktop
