import dataset

db = dataset.connect('sqlite:///example.db')

# Drop tables if they exist
db["faculty"].drop()
db["department"].drop()

# Create faculty table
faculty_table = db.create_table("faculty")
faculty_table.create_column("faculty_id", db.types.integer)
faculty_table.create_column("name", db.types.text)
faculty_table.create_column("department_id", db.types.integer)

# Create department table
department_table = db.create_table("department")
department_table.create_column("id", db.types.integer)
department_table.create_column("name", db.types.text)

# Sample data for faculty
faculty_data = [
    {"name": "Professor Smith", "department_id": 1},
    {"name": "Dr. Johnson", "department_id": 2},
    {"name": "Professor Davis", "department_id": 3},
    # Add more faculty members as needed
]

# Insert faculty data
faculty_table.insert_many(faculty_data)

# Sample data for departments
department_data = [
    {"name": "Computer Science"},
    {"name": "Physics"},
    {"name": "History"},
]

# Insert department data
department_table.insert_many(department_data)

print("Data inserted successfully.")