from flask import Flask, request, render_template, url_for

app = Flask(__name__)


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')


@app.route('/value', methods=["GET", "POST"])
def count():
    if request.method == 'POST':
        x = request.form['www']
        return render_template('value.html', result=x)
    else:
        return render_template('value.html')


@app.route('/check', methods=["GET"])
def ipynb_page():
    return render_template('cycle.html')


if __name__ == "__main__":
    app.run()
