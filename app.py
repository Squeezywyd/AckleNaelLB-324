from flask import Flask, render_template, request, redirect, url_for, session, flash
from datetime import datetime
from dataclasses import dataclass, field
import os
from dotenv import load_dotenv

# Flask-App
app = Flask(__name__)
app.secret_key = os.urandom(24)

# .env laden (lokal) / auf Azure kommt PASSWORD aus App Settings
load_dotenv()
PASSWORD = os.getenv("PASSWORD", "")

# In-Memory-Speicher
entries = []


@dataclass
class Entry:
    content: str
    happiness: str = ""                       # NEU: Happiness-Feld
    timestamp: datetime = field(default_factory=datetime.now)  # korrekter Default


@app.route("/", methods=["GET"])
def index():
    return render_template("index.html", entries=entries)


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        user_password = request.form.get("password", "")
        if user_password == PASSWORD:
            session["logged_in"] = True
            flash("Login successful!", "success")
            return redirect(url_for("index"))
        else:
            flash("Incorrect password. Please try again.", "error")
    return render_template("login.html")


@app.route("/logout")
def logout():
    session.pop("logged_in", None)
    flash("Logged out successfully.", "success")
    return redirect(url_for("index"))


@app.route("/add_entry", methods=["POST"])
def add_entry():
    content = request.form.get("content", "").strip()
    happiness = request.form.get("happiness", "").strip()   # NEU: aus Formular lesen

    if content:
        # NEU: Jüngster Eintrag zuerst (entries[0]) – wichtig für den Test
        entries.insert(0, Entry(content=content, happiness=happiness))

    # WICHTIG: explizit "/" redirecten (der Test erwartet exakt diese Location)
    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)
