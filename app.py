from flask import Flask, render_template

app = Flask(__name__)

SITE_NAME = "Kitchen Chemistry"
TAGLINE = "Where cooking meets chemistry"


@app.context_processor
def inject_globals():
    return dict(site_name=SITE_NAME, tagline=TAGLINE)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/science")
def science():
    return render_template("science.html")


@app.route("/experiments")
def experiments():
    return render_template("experiments.html")


@app.route("/mysteries")
def mysteries():
    return render_template("mysteries.html")


@app.route("/quiz")
def quiz():
    return render_template("quiz.html")


@app.route("/creds")
def creds():
    return render_template("creds.html")


@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404


if __name__ == "__main__":
    app.run(debug=True)
