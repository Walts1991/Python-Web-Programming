'''
www.getbootstrap.com
download
extract all
save all files in static folder on server

update HTML file to include:
<head>
    <link href="/static/css/bootstrap.min.css" rel="stylesheet"
    media="screen">
</head>

preference within Flask is to use variables (dynamic) using {{use_for}}:
<head>
    <link href="{{ url_for('static',filename='css/bootstrap.min.css') }}" rel="stylesheet"
    media="screen">
</head>

Review Bootstrap for examples of what can be included
'''