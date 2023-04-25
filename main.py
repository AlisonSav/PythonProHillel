from flask import Flask
from random import randint

app = Flask(__name__)

lst = [1, 2, 3, 4, 5]


@app.route("/")
def show_items():
    return f"<h3>Values in list are: {lst}<h3>"


@app.route("/add_item")
def add_item():
    lst.append(randint(1, 100))
    return f"<h3>Updated list: {lst}<h3>"


@app.route("/delete_item")
def delete_item():
    return f"<h3>Deleted item is: {lst.pop()}<h3>"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)
