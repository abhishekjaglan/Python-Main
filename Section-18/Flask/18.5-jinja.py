from flask import Flask, redirect,render_template, request, url_for

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

@app.route('/submit', methods=['POST'])
def submit():
    name=request.form['name']
    return f"Hello {name} from /submit"

## Variable rule
@app.route('/success/<int:score>') ## defining data type of query parameter
def success(score):
    return 'Your score is ' + str(score)

## jinja passing props
@app.route('/result/<int:score>')
def result(score):
    res=''
    if score >= 50:
        res="passed"
    else:
        res="failed"
    return render_template('result.html', result=res ,score=score)

## jinja2 template
'''
{{ }} expression to print passed parameter in html
{%...%} conditions, for loops
{#...#} comments in jinja
'''
## for and if condition used in template frontend
@app.route('/resultexp/<int:score>')
def resultexp(score):
    res=''
    if score >= 50:
        res="passed"
    else:
        res="failed"

    exp={'score':score, 'result':res}
    print(type(score))
    print(type(res))
    return render_template('result1.html', result=res ,score=score, exp=exp)

##dynamic URL
@app.route('/submitres', methods=['POST', 'GET'])
def submitres():
    total_score=0
    if request.method=='POST':
        total_score+=float(request.form['science'])
        print(total_score)
        total_score+=float(request.form['datascience'])
        print(total_score)
        total_score+=float(request.form['maths'])
        print(total_score)
        total_score+=float(request.form['python'])
        print(total_score)
        total_score/=4
        print(total_score)
    else:
        return render_template('getresult.html')
    return redirect(url_for('resultexp',score=total_score))

if __name__ == '__main__':
    app.run(port=2024, debug=True)