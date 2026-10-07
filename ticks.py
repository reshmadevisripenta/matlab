import matplotlib.pyplot as plt

months = ["January", "February", "March", "April", "May"]
revenue = [20, 40, 60, 80, 100]

plt.plot(months, revenue, marker="o")

plt.xticks(rotation=45)
plt.yticks([0, 20, 40, 60, 80, 100])

plt.xlabel("Months")
plt.ylabel("Revenue")
plt.title("Monthly Revenue")

plt.grid(True)
plt.show()
