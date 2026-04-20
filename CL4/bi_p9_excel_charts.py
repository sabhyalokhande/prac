import matplotlib.pyplot as plt
import numpy as np

# Sample data (like Excel)
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']
sales = [15000, 18000, 12000, 22000, 19000, 25000]
expenses = [10000, 12000, 9000, 14000, 13000, 16000]
profit = [s - e for s, e in zip(sales, expenses)]

fig, axes = plt.subplots(2, 3, figsize=(15, 10))

# STEP 2: Column Chart
axes[0, 0].bar(months, sales, color='steelblue')
axes[0, 0].set_title('Column Chart - Sales')
axes[0, 0].set_ylabel('Amount')

# STEP 3: Bar Chart
axes[0, 1].barh(months, expenses, color='orange')
axes[0, 1].set_title('Bar Chart - Expenses')

# STEP 4: Line Chart
axes[0, 2].plot(months, profit, marker='o', color='green', linewidth=2)
axes[0, 2].set_title('Line Chart - Profit')
axes[0, 2].set_ylabel('Profit')

# STEP 5: Pie Chart
axes[1, 0].pie(sales, labels=months, autopct='%1.1f%%', startangle=90)
axes[1, 0].set_title('Pie Chart - Sales Distribution')

# STEP 6: Scatter Plot
axes[1, 1].scatter(sales, expenses, color='purple', s=100)
axes[1, 1].set_title('Scatter Plot - Sales vs Expenses')
axes[1, 1].set_xlabel('Sales')
axes[1, 1].set_ylabel('Expenses')

# STEP 7: Waterfall Chart
cumulative = [0] + list(np.cumsum(profit))
colors = ['green' if p >= 0 else 'red' for p in profit]
for i, (p, c) in enumerate(zip(profit, colors)):
    axes[1, 2].bar(i, abs(p), bottom=min(cumulative[i], cumulative[i+1]), color=c)
axes[1, 2].set_xticks(range(len(months)))
axes[1, 2].set_xticklabels(months)
axes[1, 2].set_title('Waterfall Chart - Profit')

plt.tight_layout()
plt.savefig("bi_p9_charts.png")
plt.show()
print("All charts saved to bi_p9_charts.png")
