import matplotlib.pyplot as plt

months = ["Jan", "Feb", "Mar", "Apr"]
sales = [20, 35, 25, 40]
plt.plot(months, sales)
plt.savefig("sales_chart.png")