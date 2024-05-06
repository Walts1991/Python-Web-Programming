from flask import Flask, render_template

app = Flask(__name__) #name of app e.g. if name = main

@app.route('/') #if on a page e.g. google.com/ - / is decorator
def homepage():
    try:
        name = "Python"
        example_list = ["2.5", "2.6", "2.7", "3.1", "3.3", "3.4"]
        return render_template('index.html', name = name, example_list = example_list)
    except Exception as e:
        return str(e)

if __name__ == "__main__":
    app.run(host='46.101.82.121')
