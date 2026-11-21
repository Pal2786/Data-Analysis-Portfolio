
import pandas as pd
import matplotlib.pyplot as plt

# Load fictional operational data
df = pd.read_csv("sample_data.csv")
df["date"] = pd.to_datetime(df["date"])

# Calculate performance indicators
df["net_movement"] = df["new_cases"] - df["resolved_cases"]
df["cumulative_change"] = df["net_movement"].cumsum()

print("Total new cases:", df["new_cases"].sum())
print("Total resolved cases:", df["resolved_cases"].sum())
print("Net workload change:", df["net_movement"].sum())

# Create a workload trend chart
plt.plot(df["date"], df["new_cases"], label="New cases")
plt.plot(df["date"], df["resolved_cases"], label="Resolved cases")

plt.title("Operational Workload Trends")
plt.xlabel("Date")
plt.ylabel("Number of cases")
plt.legend()
plt.xticks(rotation=45)
plt.tight_layout()

plt.savefig("workload_trends.png")
plt.show()
