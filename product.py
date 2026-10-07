import matplotlib.pyplot as plt
product=["laptop","desktop","keyboard"]
sales=[120000,150000,100000]
plt.bar(product,sales)
plt.xlabel("Product")
plt.ylabel("Sales")
plt.title("Product Sales")
plt.show()