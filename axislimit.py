import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [20, 40, 60, 80, 90]

plt.plot(x, y, marker="o")

plt.xlim(0, 10)
plt.ylim(0, 100)

plt.xlabel("X Values")
plt.ylabel("Y Values")
plt.title("X and Y Limits")

plt.grid(True)
plt.show()