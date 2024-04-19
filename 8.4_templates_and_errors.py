'''
Error handling and templates
FileZilla
/var/www/FlaskApp/FlaskApp directory
Way to edit fiels without dragging/dropping from desktop
edit - settings - file editing
set filetype associations to determine which program to edit file types directly from FileZilla
To show error message use error handling e.g. in __init__.py within def homepage():
try:
    return "Hello World"
except Exception as e:
    return(str(e))

within templates folder in FileZilla
Create new index.html file
Add html code to index.html e.g.
<!DOCTYPE html>
<html>
    <p>
        Hey, that worked!
    </p>
</html>

service apache2 restart
test website ip address
'''