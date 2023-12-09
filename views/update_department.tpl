<!DOCTYPE html>
<html>
<head>
    <title>Update Department</title>
</head>
<body>
    <h1>Update Department</h1>
    <form action="/update_department" method="post">
        <input type="hidden" name="department_id" value="{{ department['id'] }}">

        <label for="name">Name:</label>
        <input type="text" id="name" name="name" value="{{ department['name'] }}" required>
        <br>

        <input type="submit" value="Update Department">
    </form>
    <br>
    <a href="/list">Back to List</a>
</body>
</html>
