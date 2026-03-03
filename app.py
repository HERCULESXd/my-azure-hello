from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello World!Jay this side from CS DEPARTMENT"

if __name__ == "__main__":
    app.run()
