import numpy as np
import csv

# using loadtxt()
arr = np.loadtxt("student_grades.csv",
				delimiter=",", dtype=str,)
print(arr)
