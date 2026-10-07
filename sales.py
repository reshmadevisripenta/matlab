import matplotlib.pyplot as plt
months=["jan","feb","mar","apr","may"]
sales_2025=[100,234,129,90,87]
sales_2026=[200,300,400,500,600]
plt.plot(months,sales_2025,label="sales in 2025",marker="X")
plt.plot(months,sales_2026,label="sales in 2026",marker="^")
plt.title("monthly sales")
plt.xlabel("months")
plt.ylabel("sales")
plt.legend()
plt.show()