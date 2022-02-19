from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

app.run("127.0.0.1", 8080, debug=True)