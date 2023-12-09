<!DOCTYPE html>
<html>
<head>
    <title>Add Department</title>
</head>
<body>
    <h1>Add Department</h1>
    <form action="/add_department" method="post">
        <label for="name">Name:</label>
        <input type="text" id="name" name="name" required>
        <br>

        <input type="submit" value="Add Department">
    </form>
    <br>
    <a href="/list">Back to List</a>
</body>
</html>
