from flask import Flask, render_template, request, session, jsonify
app = Flask(
    __name__,
    template_folder="web/templates",
    static_folder="web/static"
)
app.secret_key = "secret"

from db.UserController import UserController

@app.route("/", methods=["GET"])
def home():
    banner = request.args.get("banner")

    return render_template("index.html", route="/", banner=banner)

@app.route("/dashboard", methods=["GET"])
def dashboard():
    return render_template("dashboard.html", route="/dashboard")

@app.route("/login", methods=["GET"])
def login():
    return render_template("login.html", route="/login")

@app.route("/api/user/auth", methods=["POST"])
def api_user_login():
    username = request.form.get("username")
    password = request.form.get("password")

    auth = UserController.auth_user(username, password)

    if not auth:
        return "Unauthorized", 401
    
    session["user"] = UserController.get_user(username)
    return "OK"

@app.route("/api/user/search", methods=["GET"])
def api_user_search():
    query = request.args.get("query", "")
    
    users = UserController.search_users(query)

    return jsonify(users)

app.run("127.0.0.1", 8080, debug=True)