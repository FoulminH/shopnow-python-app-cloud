import os

from flask import Flask, render_template

app = Flask(__name__)

app_version = "1.0.0"

@app.route("/")
def home():
    return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
