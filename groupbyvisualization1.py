import pandas as pd
import matplotlib.pyplot as plt

data = {
    "Name": ["Anu", "Ravi", "Kiran", "Sita", "Rahul", "Priya"],
    "Department": ["IT", "HR", "IT", "Sales", "HR", "Sales"],
    "Salary": [30000, 25000, 40000, 35000, 30000, 45000]
}

df = pd.DataFrame(data)

summary = df.groupby("Department")["Salary"].mean()

plt.bar(summary.index, summary.values)

plt.title("Average Salary by Department")
plt.xlabel("Department")
plt.ylabel("Average Salary")

plt.show()