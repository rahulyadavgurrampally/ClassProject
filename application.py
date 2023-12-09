from bottle import route, post, run, template, redirect, request
import database

@route("/")
def get_index():
    redirect("/list")

@route("/list")
def get_list():
    faculty = database.get_faculty()
    departments = database.get_departments()
    return template("list_faculty_department.tpl", faculty=faculty, departments=departments , search_faculty="")

# Faculty routes

@route("/add_faculty")
def get_add_faculty():
    departments = database.get_departments()
    return template("add_faculty.tpl", departments=departments)

@post("/add_faculty")
def post_add_faculty():
    name = request.forms.get("name")
    department_id = request.forms.get("department_id")
    database.add_faculty(name, int(department_id))
    redirect("/list")

@route("/delete_faculty/<faculty_id>")
def get_delete_faculty(faculty_id):
    database.delete_faculty(faculty_id)
    redirect("/list")

@route("/update_faculty/<faculty_id:int>")
def get_update_faculty(faculty_id):

    faculty = database.get_faculty(faculty_id)
    print(faculty)
    if len(faculty) != 1:
        redirect("/list")
    faculty_member = faculty[0]
    departments = database.get_departments()
    return template("update_faculty.tpl", faculty=faculty_member, departments=departments)

@post("/update_faculty")
def post_update_faculty():
    name = request.forms.get("name")
    department_id = request.forms.get("department_id")
    faculty_id = request.forms.get("faculty_id")
    database.update_faculty(int(faculty_id), name, int(department_id))
    redirect("/list")

# # Department routes

@route("/add_department")
def get_add_department():
    return template("add_department.tpl")

@post("/add_department")
def post_add_department():
    name = request.forms.get("name")
    database.add_department(name)
    redirect("/list")

@route("/delete_department/<department_id>")
def get_delete_department(department_id):
    database.delete_department(int(department_id))
    redirect("/list")

# Add a new route for handling faculty search
@route("/search_faculty", method="GET")
def get_search_faculty():
    search_term = request.query.get("search_faculty", "")
    faculty = database.search_faculty(search_term)
    departments = database.get_departments()
    return template("list_faculty_department.tpl", faculty=faculty, departments=departments, search_faculty=search_term)

    
# Add a new function in the database.py file to perform faculty search
def search_faculty(search_faculty):
    faculty_data = db["faculty"].find(name={"$like": f"%{search_faculty}%"})
    departments = {d['id']: d['name'] for d in db["department"].find()}
    faculty = [
        {'id': member['id'], 'name': member['name'], 'department_name': departments.get(member['department_id'], '')}
        for member in faculty_data
    ]
    return faculty


run(host='localhost', port=8080)