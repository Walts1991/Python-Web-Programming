'''
Bootstrap is responsive so care with zoom when previewing
<DOCTYPE html> - notify browsers that it is a HTML document
<html lang="en"> - notify browsers that site language is English
Could use en-gb to specify uk rather than us
col-md-1 - col-md-12 (12 columns in total is max)
Review bootstrap to see example for what is required e.g. forms
https://getbootstrap.com/docs/3.4/css/

There are also components
https://getbootstrap.com/docs/3.4/components/
Example search icon:
<span class="glyphicon glyphicon-search" aria-hidden="true"></span>

Example button dropdown:
<!-- Single button -->
<div class="btn-group">
  <button type="button" class="btn btn-default dropdown-toggle" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
    Action <span class="caret"></span>
  </button>
  <ul class="dropdown-menu">
    <li><a href="#">Action</a></li>
    <li><a href="#">Another action</a></li>
    <li><a href="#">Something else here</a></li>
    <li role="separator" class="divider"></li>
    <li><a href="#">Separated link</a></li>
  </ul>
</div>

Note some features may have dependencies such as plugins

Need to add Javascript:
Javascript usually added below section that uses it e.g. after <body> tags
<script src="//code.jquery.com/jquery-1.11.1.min.js"</script>
<script src="{{ url_for('static', filename='js/bootstrap.min.js') }}.min.js"</script>
jquery is used frequently in javascript
Bootstrap bundle is often used nowadays as per Gemini:
<script src="{{ url_for('static', filename='js/bootstrap.bundle.min.js') }}"></script>

Add Nav Bar from Bootstrap components
Can rename labels
Do not rename id's, class and types as these are built into bootstrap
Would require further changes
'''
