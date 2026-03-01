from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello World from Jay4315"

if __name__ == "__main__":
    app.run()
