from flask import Flask, render_template,  request, session
from utils import change_response, verify_age_restrition
import requests

app = Flask(__name__)
app.secret_key = "pGGZlpgfT2"


RESTRICT_KEYWORDS = [
    "CORONAVIRUS",
    "GUERRA",
    "ARMAS",
    "VIOLÊNCIA"
]


@app.route("/proxy", methods=["POST"])
def proxy():
    url = request.form["url"]
    response = requests.get(url).text
    if verify_age_restrition(response, RESTRICT_KEYWORDS, session["isOlder"]):
        return change_response(response, "/")

    return render_template("restrict_page.html")


@app.route("/", methods=["GET"])
def index():
    print(session)
    if session.get("username"):
        return render_template("index.html", username=session["username"], user_age=session["age"], restricted_words=RESTRICT_KEYWORDS)

    return render_template("login.html")


@app.route("/login", methods=["POST"])
def teste():
    if request.method == "POST":
        session["username"] = request.form["username"]
        session["age"] = request.form["age"]
        if int(request.form["age"]) > 18:
            session["isOlder"] = True
        else:
            session["isOlder"] = False

    return render_template("index.html", username=session["username"], user_age=session["age"], restricted_words=RESTRICT_KEYWORDS)


@app.route('/logout', methods=["POST"])
def logout():
    print(session)
    session.clear()
    print(session)
    return render_template("login.html")


if __name__ == "__main__":
    app.run()
