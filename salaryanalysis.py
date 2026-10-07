import pandas as pd 
import matplotlib.pyplot as plt
salary = [    25000, 28000, 30000, 32000,    35000, 36000, 38000, 40000,    
          42000, 45000, 48000, 50000,    55000, 60000, 80000, 90000,    100000, 120000, 150000, 200000] 
plt.hist(    salary,    bins=8,    edgecolor="black" ) 
plt.title("Employee Salary Distribution") 
plt.xlabel("Salary") 
plt.ylabel("Number of Employees") 
plt.show()