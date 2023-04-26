from flask import Flask
from random import randint

app = Flask(__name__)

lst = []


@app.route("/")
def show_items():
    return f"<h3>Values in list are: {lst}<h3>"


@app.route("/add_item")
def add_item():
    if len(lst) >= 10:
        return f"<h3>Sorry! You can't add value if list's length more than 10!<h3>"
    else:
        lst.append(randint(1, 100))
        return f"<h3>Updated list: {lst}<h3>"


@app.route("/delete_item")
def delete_item():
    if lst:
        return f"<h3>Deleted item is: {lst.pop()}<h3>"
    else:
        return f"<h3>Your list {lst} is empty. You can't delete value<h3>"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)
