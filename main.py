from flask import Flask, request, render_template
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def index():
    now = datetime.now()
    current_time = now.strftime("%Y-%m-%d %H:%M:%S  ")
    return render_template('home.html', name = current_time)

@app.route("/blog/")
def blog():
    now = datetime.now()
    current_time = now.strftime("%Y-%m-%d %H:%M:%S  ")
    return render_template('about.html', name = current_time)



if __name__ == '__main__':
    app.run(debug=True)