from flask import Flask, render_template

app = Flask(__name__) #name of app e.g. if name = main

@app.route('/') #if on a page e.g. google.com/ - / is decorator
def homepage():
    try:
        return render_template('index.html')
    except Exception as e:
        return(str(e))
    
if __name__ == "__main__":
    app.run(host='46.101.82.121')
