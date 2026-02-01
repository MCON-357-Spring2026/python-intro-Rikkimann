"""
TODO:
Dictionary of students -> grades
Print averages
"""
student = {"Alice": [100, 98, 67, 89],
           "Brooke": [98, 78, 98, 89],
           "Celia": [87, 76, 78, 87], }

for k, v in student.items():
    average= sum(v)/len(v)
    print(f"{k}: {average:.2f}")