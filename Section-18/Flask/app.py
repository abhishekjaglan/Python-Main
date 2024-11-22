from flask import Flask

## It creates an instance of the Flask class, which will be our WSGI (web server gateway interface) application, ## kinda like express

## initilizing the application 
app = Flask(__name__)

@app.route("/")
def welcome():
  return "Welcome to my first flask skeleton. Debug is truee nowww"

@app.route('/abhishek')
def abhishek():
  return "You are inside my function and endpoint nowwww"

## Entry point for running the application
if __name__ == "__main__":
    app.run(port=2024,debug=True)