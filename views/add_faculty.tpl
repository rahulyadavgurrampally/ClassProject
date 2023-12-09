<!DOCTYPE html>
<html>
<head>
    <title>Add Faculty</title>
</head>
<body>
    <h1>Add Faculty</h1>
    <form action="/add_faculty" method="post">
        <label for="name">Name:</label>
        <input type="text" id="name" name="name" required>
        <br>

        <label for="department_id">Department:</label>
        <select id="department_id" name="department_id">
            % for department in departments:
                <option value="{{ department['id'] }}">{{ department['name'] }}</option>
            % end
        </select>
        <br>

        <input type="submit" value="Add Faculty">
    </form>
    <br>
    <a href="/list">Back to List</a>
</body>
</html>
