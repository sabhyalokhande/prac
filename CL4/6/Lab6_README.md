# Lab Practical 6 — Import Data from Different Sources (Power BI)

**Aim:** Import Data from different sources such as Excel, SQL Server, OData Feed etc. and load in targeted system using Power BI Desktop.

---

## How to Open Power BI Desktop

1. Press **Windows** key → search **Power BI Desktop** → click to open
2. Sign in with your Microsoft account (optional for desktop use)
3. You will see the **Start screen** — close it or click **Get started**
4. The main window opens with **Home**, **Insert**, **Modeling**, **View** ribbons at the top

---

## Part A: Import Data from Excel

### Step 1: Launch Power BI Desktop

Open Power BI Desktop from the Start menu.

---

### Step 2: Get Data

From the **Home** ribbon, select **Get Data**.

You will see common data sources:
- Excel workbook
- Power BI semantic models
- SQL Server
- Text/CSV
- Web
- OData feed
- More...

---

### Step 3: Select Excel File

In the **Open File** dialog box, browse and select the `Products.xlsx` file (or `Superstore_Sample.xlsx`).

Click **Open**.

---

### Step 4: Select Table in Navigator

In the **Navigator** pane:
- Select the **Products** table (or **Superstore** sheet)
- Click **Transform Data** to open Power Query Editor, or **Load** to load directly

---

## Part B: Import Data from OData Feed

OData Feed URL:
```
http://services.odata.org/V3/Northwind/Northwind.svc/
```

### Step 1: Get Data → OData Feed

From the **Home** ribbon tab in Query Editor, select **Get Data**.

Browse to **OData Feed** data source and click **Connect**.

---

### Step 2: Enter OData URL

In the **OData Feed** dialog box:
- Select **Basic**
- Paste the URL:
  ```
  http://services.odata.org/V3/Northwind/Northwind.svc/
  ```
- Click **OK**

---

### Step 3: Select Table in Navigator

In the **Navigator** pane:
- Select the **Orders** table
- Click **Transform Data** to open in Power Query Editor

The Orders table will load with columns:
- OrderID, CustomerID, EmployeeID
- OrderDate, RequiredDate, ShippedDate
- ShipVia, Freight, ShipName, ShipAddress
- ShipCity, ShipRegion, ShipPostalCode

---

## Summary: Supported Data Sources in Power BI

| Source | How to Connect |
|---|---|
| Excel (.xlsx) | Get Data → Excel workbook → select file |
| SQL Server | Get Data → SQL Server → enter server/db name |
| OData Feed | Get Data → OData feed → paste URL |
| Text/CSV | Get Data → Text/CSV → select file |
| Web | Get Data → Web → paste URL |
| Oracle | Get Data → More → Oracle database |

---

## Result

Data from Excel (Superstore) and OData Feed (Northwind Orders) successfully imported and loaded into Power BI Desktop for further transformation and visualization.
