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

Review Bootstrap for examples of what can be included e.g. grid below
    <div class="row">
        <div class="col-md-1">.col-md-1</div>
        <div class="col-md-1">.col-md-1</div>
        <div class="col-md-1">.col-md-1</div>
        <div class="col-md-1">.col-md-1</div>
        <div class="col-md-1">.col-md-1</div>
        <div class="col-md-1">.col-md-1</div>
        <div class="col-md-1">.col-md-1</div>
        <div class="col-md-1">.col-md-1</div>
        <div class="col-md-1">.col-md-1</div>
        <div class="col-md-1">.col-md-1</div>
        <div class="col-md-1">.col-md-1</div>
        <div class="col-md-1">.col-md-1</div>
      </div>
      <div class="row">
        <div class="col-md-8">.col-md-8</div>
        <div class="col-md-4">.col-md-4</div>
      </div>
      <div class="row">
        <div class="col-md-4">.col-md-4</div>
        <div class="col-md-4">.col-md-4</div>
        <div class="col-md-4">.col-md-4</div>
      </div>
      <div class="row">
        <div class="col-md-6">.col-md-6</div>
        <div class="col-md-6">.col-md-6</div>
      </div>
'''