from flask import Flask, request, url_for, Response, render_template

app = Flask(__name__)

@app.route('/')
@app.route('/news')
def index():
    return render_template("index.html")

@app.route('/contact')
@app.route('/news/contact')
def contact():
    return render_template("contact.html")

if __name__ == '__main__':
    app.run()