<!DOCTYPE html>
<html>
<head>
    <title>Faculty and Department List</title>
</head>
<body>
    <h1>Faculty and Department List</h1>
    <form action="/search_faculty" method="get">
    <label for="search_faculty">Search Faculty:</label>
    <input type="text" name="search_faculty" value="{{ search_faculty }}">
    <input type="submit" value="Search">
    </form>

    % if search_faculty:
        <h2>Search Results for '{{ search_faculty }}'</h2>
        % if faculty:
            <h3>Faculty Information:</h3>
            % for member in faculty:
                <p>{{ member['name'] }} - {{ member['department_name'] }}</p>
            % end
        % else:
            <p>No faculty found with the name '{{ search_faculty }}'</p>
        % end
    % else:
        <h2>Faculty List</h2>
        <ul>
            % for faculty_member in faculty:
                <li>{{ faculty_member['name'] }} - ID is {{ faculty_member['id'] }}
                    (<a href="/update_faculty/{{ faculty_member['id'] }}">Update</a>,
                    <a href="/delete_faculty/{{ faculty_member['id'] }}">Remove</a>)
                </li>
            % end
        </ul>

        <h2>Department List</h2>
        <ul>
            % for department in departments:
                <li>{{ department['name'] }} - ID is {{ department['id'] }}
                    (<a href="/delete_department/{{ department['id'] }}">Remove</a>)
                </li>
            % end
        </ul>

        <h2>Faculty and Department List</h2>
        <ul>
            % for faculty_member in faculty:
                <li>{{ faculty_member['name'] }} - {{ faculty_member['department_name'] }}
                </li>
            % end 
        </ul>

        <h2>Add Faculty</h2>
        <a href="/add_faculty">Add Faculty</a>

        <h2>Add Department</h2>
        <a href="/add_department">Add Department</a>
    % end
</body>
</html>
