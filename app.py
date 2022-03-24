from flask import Flask, redirect, render_template, request, session, jsonify
from db.AnnouncementsController import AnnouncementsController
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

    unread_announcements = AnnouncementsController.count_unreads(session["user"]["username"])
    
    return render_template("dashboard/index.html", route="/dashboard", page="home", banner=banner, unreads=unread_announcements)

@app.route("/dashboard/announcements", methods=["GET"])
def dashboard_announcements():
    if "user" not in session.keys():
        return redirect("/login")

    unread_announcements = AnnouncementsController.count_unreads(session["user"]["username"])

    announcements = AnnouncementsController.get_unreads(session["user"]["username"])
    
    return render_template("dashboard/announcements.html", route="/dashboard", page="announcements", unreads=unread_announcements, announcements=announcements)

@app.route("/dashboard/hours", methods=["GET"])
def dashboard_hours():
    if "user" not in session.keys():
        return redirect("/login")

    unread_announcements = AnnouncementsController.count_unreads(session["user"]["username"])
    
    return render_template("dashboard/index.html", route="/dashboard", page="hours", unreads=unread_announcements)

@app.route("/dashboard/holidays", methods=["GET"])
def dashboard_holidays():
    if "user" not in session.keys():
        return redirect("/login")

    unread_announcements = AnnouncementsController.count_unreads(session["user"]["username"])
    
    return render_template("dashboard/index.html", route="/dashboard", page="holidays", unreads=unread_announcements)

@app.route("/dashboard/links", methods=["GET"])
def dashboard_links():
    if "user" not in session.keys():
        return redirect("/login")

    unread_announcements = AnnouncementsController.count_unreads(session["user"]["username"])
    
    return render_template("dashboard/index.html", route="/dashboard", page="links", unreads=unread_announcements)

@app.route("/dashboard/people", methods=["GET"])
def dashboard_people():
    if "user" not in session.keys():
        return redirect("/login")

    unread_announcements = AnnouncementsController.count_unreads(session["user"]["username"])
    
    return render_template("dashboard/people.html", route="/dashboard", page="people", unreads=unread_announcements)

@app.route("/dashboard/admin/users", methods=["GET"])
def dashboard_admin_users():
    if "user" not in session.keys():
        return redirect("/login")

    if not session["user"]["admin"]:
        return redirect("/dashboard")

    unread_announcements = AnnouncementsController.count_unreads(session["user"]["username"])
    
    return render_template("dashboard/user_management.html", route="/dashboard", page="user_management", unreads=unread_announcements)

@app.route("/dashboard/admin/announcements", methods=["GET"])
def dashboard_admin_announcements():
    if "user" not in session.keys():
        return redirect("/login")

    if not session["user"]["admin"]:
        return redirect("/dashboard")

    announcement = request.args.get("name")

    unread_announcements = AnnouncementsController.count_unreads(session["user"]["username"])
    
    return render_template("dashboard/post_announcement.html", route="/dashboard", page="post_announcement", unreads=unread_announcements, announcement=announcement)

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

@app.route("/api/admin/user", methods=["POST"])
def api_admin_user_create():
    body = request.get_json()
    
    UserController.create_user(
        body["firstName"],
        body["lastName"],
        body["jobTitle"],
        body["email"],
        body["admin"],
        body["username"],
        body["password"],
    )

    return "Created", 201

@app.route("/api/admin/user", methods=["PUT"])
def api_admin_user_edit():
    body = request.get_json()
    
    UserController.edit_user(
        body["oldUsername"],
        body["firstName"],
        body["lastName"],
        body["jobTitle"],
        body["email"],
        body["admin"],
        body["username"]
    )

    return "OK"

@app.route("/api/announcements/read", methods=["POST"])
def api_announcements_read():
    AnnouncementsController.mark_as_read(session["user"]["username"])

    return ""

@app.route("/api/admin/announcement", methods=["POST"])
def api_admin_announcement():
    body = request.get_json()
    
    AnnouncementsController.create_announcement(body["title"], body["text"], session["user"]["username"])

    return "Created", 201

@app.errorhandler(404)
def error_404(e):
    return render_template("404.html")

app.run("127.0.0.1", 8080, debug=True)