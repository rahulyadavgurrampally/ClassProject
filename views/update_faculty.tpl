<!DOCTYPE html>
<html>
<head>
    <title>Update Faculty</title>
</head>
<body>
    <h1>Update Faculty</h1>
    <form action="/update_faculty" method="post">
        <input type="hidden" name="faculty_id" value="{{ faculty['id'] }}">

        <label for="name">Name:</label>
        <input type="text" id="name" name="name" value="{{ faculty['name'] }}" required>
        <br>

        <label for="department_id">Department:</label>
        <select id="department_id" name="department_id">
            % for department in departments:
                <option value="{{ department['id'] }}" % if faculty['department_id'] == department['id']: selected % end>{{ department['name'] }}</option>
            % end
        </select>
        <br>

        <input type="submit" value="Update Faculty">
    </form>
    <br>
    <a href="/list">Back to List</a>
</body>
</html>
