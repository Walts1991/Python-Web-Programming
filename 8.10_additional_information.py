"""
Add error handling page for 404 error within __init__.py:
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html')

Create 404.html page with error message text to be displayed to user

Add div class container to body text to contain text:
  <div class="container">
  {% block body %} {% endblock %}
  </div>

Add button to top of page-one.html:
    <button type="button" class="btn btn-primary">Action</button>
Button made by bootstrap with styling etc.
primary relates to colour and can see colour options within bootstrap examples:
e.g. default, primary, success, info, warning, danger
Can also change primary to {{button_type}} and add variable to __init__.py
Under pageone function, under try, add button_type = '[type]' e.g. info
and add keyword argument to render_template:
    try:
        button_type = 'info'
        name = "Python"
        example_list = ["2.5", "2.6", "2.7", "3.1", "3.3", "3.4"]
        return render_template('page-one.html', button_type = button_type, name = name, example_list = example_list)
"""
