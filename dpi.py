import matplotlib.pyplot as plt

months = ["Jan", "Feb", "Mar", "Apr"]
sales = [20, 35, 25, 40]

plt.plot(months, sales, marker="o")

plt.title("Sales Chart")
plt.xlabel("Months")
plt.ylabel("Sales")

plt.tight_layout()

plt.savefig(
    "sales_chart.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()