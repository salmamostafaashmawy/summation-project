
from flask import Flask , render_template, request

app = Flask(__name__)


@app.route("/")
def index():
    return render_template('index.html')

@app.route("/sum", methods=["GET","POST"])
def sum():
    x=float(request.form.get('x'))
    y=float(request.form.get('y'))
    sum=x+y
    return render_template('index.html',sum=sum)


if __name__ == '__main__':
    app.run(port=5000)