from flask import Flask,render_template, request

app = Flask(__name__)

@app.route('/home') ## GET by default
def home():
    return 'This the home page boys and chicaas'

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/abhishek', methods=['GET'])
def abhishek():
    return render_template('index.html')

@app.route('/form', methods=['GET','POST'])
def form():
    if request.method=='POST':
        name=request.form['name']
        return f"Hello {name}"
    return render_template('form.html')

if __name__ == '__main__':
    app.run(port=2024, debug=True)