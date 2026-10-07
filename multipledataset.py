import matplotlib.pyplot as plt

class_a = [45, 50, 55, 60, 62, 65, 70, 72, 75, 80]
class_b = [40, 48, 52, 58, 63, 67, 70, 76, 78, 85]

plt.hist(class_a, bins=5, alpha=0.5, label="Class A")
plt.hist(class_b, bins=5, alpha=0.5, label="Class B")

plt.xlabel("Marks")
plt.ylabel("Number of Students")
plt.title("Class A vs Class B Marks")

plt.legend()
plt.show()