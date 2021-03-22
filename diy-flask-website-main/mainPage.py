from flask import Flask, render_template
import json

app = Flask(__name__)

@app.route("/")
def home():
  return render_template("home.html")

@app.route("/new-page")
def pageTwo():
    return render_template("newPage.html")
@app.route("/dynamic/<example>")
def dynamic(example):
  with open("data.json", "r") as read_file:
    data = json.load(read_file)
  data.append(example)

  with open("data.json", "w") as json_file:
    json.dump(data, json_file)

  return "This is example: " + example

if __name__ == "__main__":
  app.run(debug=True)