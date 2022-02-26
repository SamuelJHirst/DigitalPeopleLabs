from flask import Flask, redirect, render_template, request, session, jsonify
app = Flask(
    __name__,
    template_folder="web/templates",
    static_folder="web/static"
)
app.secret_key = "secret"

from db.UserController import UserController

@app.route("/", methods=["GET"])
def home():
    return render_template("index.html", route="/")

@app.route("/dashboard", methods=["GET"])
def dashboard():
    if "user" not in session.keys():
        return redirect("/login")

    banner = request.args.get("banner")
    
    return render_template("dashboard/index.html", route="/dashboard", page="home", banner=banner)

@app.route("/dashboard/announcements", methods=["GET"])
def dashboard_announcements():
    if "user" not in session.keys():
        return redirect("/login")
    
    return render_template("dashboard/index.html", route="/dashboard", page="announcements")

@app.route("/dashboard/hours", methods=["GET"])
def dashboard_hours():
    if "user" not in session.keys():
        return redirect("/login")
    
    return render_template("dashboard/index.html", route="/dashboard", page="hours")

@app.route("/dashboard/holidays", methods=["GET"])
def dashboard_holidays():
    if "user" not in session.keys():
        return redirect("/login")
    
    return render_template("dashboard/index.html", route="/dashboard", page="holidays")

@app.route("/dashboard/links", methods=["GET"])
def dashboard_links():
    if "user" not in session.keys():
        return redirect("/login")
    
    return render_template("dashboard/index.html", route="/dashboard", page="links")

@app.route("/dashboard/people", methods=["GET"])
def dashboard_people():
    if "user" not in session.keys():
        return redirect("/login")
    
    return render_template("dashboard/people.html", route="/dashboard", page="people")

@app.route("/dashboard/admin/users", methods=["GET"])
def dashboard_admin_users():
    if "user" not in session.keys():
        return redirect("/login")

    if not session["user"]["admin"]:
        return redirect("/dashboard")
    
    return render_template("dashboard/user_management.html", route="/dashboard", page="user_management")

@app.route("/login", methods=["GET"])
def login():
    if "user" in session.keys():
        return redirect("/dashboard")

    return render_template("login.html", route="/login")

@app.route("/auth/logout", methods=["GET"])
def auth_logout():
    if "user" in session.keys():
        del session["user"]

    return redirect("/")

@app.route("/api/user/login", methods=["POST"])
def api_user_login():
    username = request.form.get("username")
    password = request.form.get("password")

    auth = UserController.auth_user(username, password)

    if not auth:
        return "Unauthorized", 401
    
    session["user"] = UserController.get_user(username)
    return "OK"

@app.route("/api/user/get", methods=["GET"])
def api_user_get():
    query = request.args.get("query", "")
    
    user = UserController.get_user(query)

    if user is None:
        return "Not found", 404

    return jsonify(user)

@app.route("/api/user/search", methods=["GET"])
def api_user_search():
    query = request.args.get("query", "")
    
    users = UserController.search_users(query)

    return jsonify(users)

@app.errorhandler(404)
def error_404(e):
    return render_template("404.html")

app.run("127.0.0.1", 8080, debug=True)