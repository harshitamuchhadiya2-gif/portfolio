from flask import Flask, render_template, send_from_directory, jsonify
from profile_data import PROFILE

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html", p=PROFILE)


@app.route("/resume")
def resume():
    return send_from_directory("static", "Harshita_Muchhadiya_Resume.pdf", as_attachment=True)


@app.route("/api/profile")
def api_profile():
    return jsonify(PROFILE)


if __name__ == "__main__":
    app.run(debug=True)
