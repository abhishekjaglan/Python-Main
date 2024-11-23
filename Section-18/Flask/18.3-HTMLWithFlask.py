from flask import Flask, render_template ## reroutes to the html page in templates using jinja2

## It creates an instance of the Flask class, which will be our WSGI (web server gateway interface) application, ## kinda like express

## initilizing the application 
app = Flask(__name__)

@app.route("/")
def welcome():
  return "<HTML><H1>Welcome to my learning of flask!!</H1></HTML>"

@app.route('/about')
def about():
   return render_template('about.html')
   

@app.route('/abhishek')
def abhishek():
  return render_template('index.html') # looks for this file in folder 'templates' inside the same folder

## Entry point for running the application
if __name__ == "__main__":
    app.run(port=2024,debug=True)