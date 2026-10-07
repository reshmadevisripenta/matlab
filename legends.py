import matplotlib.pyplot as plt

x = ["Jan", "Feb", "Mar", "Apr", "May"]

y1 = [10000, 15000, 12000, 18000, 22000]
y2 = [8000, 13000, 16000, 17000, 25000]

plt.plot(x, y1, label="Product A")
plt.plot(x, y2, label="Product B")

plt.xlabel("Months")
plt.ylabel("Revenue")
plt.title("Product Revenue Comparison")

plt.legend()
plt.show()