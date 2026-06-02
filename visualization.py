import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("sales.csv")

print(df)

plt.figure(figsize=(8,5))
plt.plot(df["Month"], df["Sales"], marker="o")
plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.grid(True)

plt.savefig("sales_chart.png")

print("Chart saved successfully!")
plt.figure(figsize=(8,5))
plt.bar(df["Month"], df["Sales"])
plt.title("Monthly Sales Bar Chart")
plt.xlabel("Month")
plt.ylabel("Sales")

plt.savefig("sales_bar_chart.png")

print("Bar chart saved successfully!")