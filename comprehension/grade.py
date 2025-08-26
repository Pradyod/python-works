grades = {'Alice': 85, 'Bob': 59, 'Charlie': 72, 'David': 45, 'Eve': 90}

above_sixty={name:grade for name,grade in grades.items() if grade>60}

print(above_sixty)