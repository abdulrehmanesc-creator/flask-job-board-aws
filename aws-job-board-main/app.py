from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>Job Board</h1><p>Software Engineer</p><p>Cloud Engineer</p>"

app.run(host="0.0.0.0", port=80)
