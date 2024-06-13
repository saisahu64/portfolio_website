from flask import Flask, redirect
app = Flask(__name__)

@app.route('/')
def landing_page():
    return redirect("/static/landing_page.html", code=302)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001, debug=True)