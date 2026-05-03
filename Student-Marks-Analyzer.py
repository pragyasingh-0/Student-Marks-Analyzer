import numpy as np  

print("Student Marks Analyzer")

n = int(input("Enter number of students: "))
marks = []

for i in range(n):
    score = float(input(f"Enter marks for student {i+1}: "))
    marks.append(score)

marks = np.array(marks)

print("\n--- Results ---")
print("Marks:", marks)
print("Average:", np.mean(marks))
print("Highest:", np.max(marks))
print("Lowest:", np.min(marks))
print("Median:", np.median(marks))

pass_count = np.sum(marks >= 40)
fail_count = np.sum(marks < 40)

print("Passed:", pass_count)
print("Failed:", fail_count)

print("\n--- Grades ---")
for mark in marks:
    if mark >= 90:
        print(mark, ": A")
    elif mark >= 75:
        print(mark, ": B")
    elif mark >= 60:
        print(mark, ": C")
    elif mark >= 40:
        print(mark, ": D")
    else:
        print(mark, ": F")
        