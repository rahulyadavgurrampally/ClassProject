import dataset

db = dataset.connect('sqlite:///example.db')

try:
    db["faculty"].drop()
    db["department"].drop()
except:
    pass

faculty_table = db["faculty"]
department_table = db["department"]

faculty_data = [
    {"faculty_id": 1, "name": "Professor Smith", "department_id": 1},
    {"faculty_id": 2, "name": "Dr. Johnson", "department_id": 2},
    {"faculty_id": 3, "name": "Professor Davis", "department_id": 3},
]

department_data = [
    {"id": 1, "name": "Computer Science"},
    {"id": 2, "name": "Physics"},
    {"id": 3, "name": "History"},
]
faculty_table.insert_many(faculty_data)
department_table.insert_many(department_data)
print("Data inserted successfully.")
