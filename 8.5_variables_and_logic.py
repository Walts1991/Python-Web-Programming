'''
Ginger 2 templating capabilities with Flask
Update __init__.py file:
name = "Python"
example_list = ["2.5", "2.6", "2.7", "3.1", "3.3", "3.4"]
return render_template('index.html', name = name, exmaple_list = example_list)
save to server
service apache2 restart

update index.html template file to include variable
Variables denoted by {{variable}} 
{{name}}
service apache2 restart (if necessary)

to include logic use {% %}
e.g. if statements, for loops etc
if, else, elif
for loop example:
{% for ver in example_list %}
    <p>{{ver}}</p>
{% endfor %}


'''
from flask import Flask, render_template

app = Flask(__name__) #name of app e.g. if name = main

@app.route('/') #if on a page e.g. google.com/ - / is decorator
def homepage():
    try:
        name = "Python"
        example_list = ["2.5", "2.6", "2.7", "3.1", "3.3", "3.4"]
        return render_template('index.html', name = name, exmaple_list = example_list)
    except Exception as e:
        return(str(e))
    
if __name__ == "__main__":
    app.run(host='46.101.82.121')
