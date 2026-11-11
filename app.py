from pathlib import Path
import os, sqlite3
from flask import Flask, flash, redirect, render_template, request, send_from_directory, url_for
BASE = Path(__file__).resolve().parent
DB = BASE / "instance" / "portfolio.db"
app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY", "replace-this-development-secret")

def db():
    DB.parent.mkdir(exist_ok=True)
    con = sqlite3.connect(DB)
    con.row_factory = sqlite3.Row
    return con

def init_db():
    with db() as con:
        con.execute("""CREATE TABLE IF NOT EXISTS messages (
            id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT NOT NULL,
            email TEXT NOT NULL, subject TEXT, message TEXT NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP)""")

@app.context_processor
def globals_for_templates():
    return {"current_year": 2026}

@app.route("/")
def home(): return render_template("home.html", page_title="Home")
@app.route("/about")
def about(): return render_template("about.html", page_title="About")
@app.route("/projects")
def projects(): return render_template("projects.html", page_title="Projects")
@app.route("/skills")
def skills(): return render_template("skills.html", page_title="Skills")
@app.route("/experience")
def experience(): return render_template("experience.html", page_title="Experience")

@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        data = {k: request.form.get(k, "").strip() for k in ("name","email","subject","message")}
        if not data["name"] or not data["email"] or not data["message"]:
            flash("Name, email and message are required.", "error")
            return render_template("contact.html", page_title="Contact"), 400
        if any(len(data[k]) > limit for k, limit in (("name",100),("email",150),("subject",150),("message",5000))):
            flash("Please shorten one or more fields.", "error")
            return render_template("contact.html", page_title="Contact"), 400
        with db() as con:
            con.execute("INSERT INTO messages(name,email,subject,message) VALUES(?,?,?,?)",
                        (data["name"],data["email"],data["subject"],data["message"]))
        flash("Message saved. Thanks for reaching out!", "success")
        return redirect(url_for("contact"))
    return render_template("contact.html", page_title="Contact")

@app.route("/resume")
def resume():
    folder = BASE / "static" / "files"
    filename = "Aranyan_T_Resume.pdf"
    if not (folder / filename).exists():
        flash("Add static/files/Aranyan_T_Resume.pdf to enable resume download.", "error")
        return redirect(request.referrer or url_for("home"))
    return send_from_directory(folder, filename, as_attachment=True)

@app.errorhandler(404)
def not_found(_): return render_template("404.html", page_title="Not found"), 404

if __name__ == "__main__":
    init_db()
    app.run(debug=True)
