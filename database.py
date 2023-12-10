import dataset

db = dataset.connect('sqlite:///example.db')

def setup_faculty_department_database():
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

def get_faculty(faculty_id=None):
    print(faculty_id)
    if faculty_id is None:
        faculty_data = db["faculty"].find()
    else:
        faculty_data = db["faculty"].find(faculty_id=int(faculty_id))
        
    departments = {d['id']: d['name'] for d in db["department"].find()}

    faculty = [
        {'id': faculty['id'], 'name': faculty['name'], 'department_name': departments.get(faculty['department_id'], '')}
        for faculty in faculty_data
    ]
    print("Found faculty:", faculty)
    
    return faculty


def get_departments():
    departments = [dict(department) for department in db["department"].find()]
    return departments

def add_faculty(name, department_id):
    db["faculty"].insert({"name": name, "department_id": department_id})

def add_department(name, department_id=None):
    if department_id is not None:
        db["department"].insert({"id": department_id, "name": name})
    else:
        db["department"].insert({"name": name})

def delete_faculty(id):
    faculty_record = db['faculty'].find_one(faculty_id=id)
    print(faculty_record)
    print(id)
    db['faculty'].delete(id=id)

def update_faculty(faculty_id, name, department_id):
    db["faculty"].update({"faculty_id": faculty_id, "name": name, "department_id": department_id}, ['faculty_id'])

def delete_department(department_id):
    db['department'].delete(id=int(department_id))
    print(f"Department with ID {department_id} deleted successfully.")

def search_faculty(search_term):
    faculty_data = db["faculty"].find(name=search_term)
    departments = {d['id']: d['name'] for d in db["department"].find()}

    faculty = [
        {'id': faculty['id'], 'name': faculty['name'], 'department_name': departments.get(faculty['department_id'], '')}
        for faculty in faculty_data
    ]

    return faculty

def test_setup_faculty_department_database():
    print("testing setup_faculty_department_database()")
    setup_faculty_department_database()

    faculty = get_faculty()
    assert len(faculty) == 3 

    departments = get_departments()
    assert len(departments) == 3 

def test_get_faculty():
    print("testing get_faculty()")
    setup_faculty_department_database()
    faculty = get_faculty()
    assert type(faculty) is list
    assert len(faculty) > 0
    for faculty_member in faculty:
        assert 'id' in faculty_member
        assert type(faculty_member['id']) is int
        assert 'name' in faculty_member
        assert type(faculty_member['name']) is str
        assert 'department_id' in faculty_member
        assert type(faculty_member['department_id']) is int

def test_get_departments():
    print("testing get_departments()")
    setup_faculty_department_database()
    departments = get_departments()
    assert type(departments) is list
    assert len(departments) > 0
    for department in departments:
        assert 'id' in department
        assert type(department['id']) is int
        assert 'name' in department
        assert type(department['name']) is str

def test_add_faculty():
    print("testing add_faculty()")
    setup_faculty_department_database()
    faculty = get_faculty()
    original_length = len(faculty)
    add_faculty("Dr. Brown", 2) 
    faculty = get_faculty()
    assert len(faculty) == original_length + 1
    names = [faculty_member['name'] for faculty_member in faculty]
    assert "Dr. Brown" in names

def test_add_department():
    print("testing add_department()")
    setup_faculty_department_database()
    departments = get_departments()
    original_length = len(departments)
    add_department("Chemistry", 4)  
    departments = get_departments()
    assert len(departments) == original_length + 1
    names = [department['name'] for department in departments]
    assert "Chemistry" in names

def test_delete_faculty():
    print("testing delete_faculty()")
    setup_faculty_department_database()
    faculty = get_faculty()
    original_length = len(faculty)
    faculty_id_to_delete = faculty[0]['faculty_id']
    delete_faculty(faculty_id_to_delete)
    faculty = get_faculty()
    assert len(faculty) == original_length - 1
    for faculty_member in faculty:
        assert faculty_member['faculty_id'] != faculty_id_to_delete

def test_update_faculty():
    print("testing update_faculty()")
    setup_faculty_department_database()
    faculty = get_faculty()
    original_name = faculty[0]['name']
    original_department_id = faculty[0]['department_id']
    faculty_id_to_update = faculty[0]['faculty_id']
    new_name = "Updated Name"
    new_department_id = 4  
    update_faculty(faculty_id_to_update, new_name, new_department_id)
    faculty = get_fac

if __name__ == "__main__":
    test_setup_faculty_department_database()
    print(get_faculty(1))
    # test_get_departments()
    # test_add_faculty()
    # test_add_department()
    # print("done.")
