import sqlite3

from flask import Flask, request
from random import randint

app = Flask(__name__)

user = None


class User:
    name = ''
    language = ''

    def __init__(self, name, language):
        self.grade = ''
        self.course = ''
        self.name = self.ascii_check(name)
        self.language = self.ascii_check(language)

    def ascii_check(self, param):
        if param.isalpha():
            return param
        else:
            raise Exception('Value contains not only letters')


def validate_alfabet(form_input, error_key, error_dict=None):
    if form_input.isalpha():
        return form_input
    error_dict[error_key] = 'Verbose error description'


def save_data(sql, user_attr_name, user_attr_value):
    setattr(user, user_attr_name, user_attr_value)
    cur.execute(sql)
    con.commit()


def is_login(func):
    def wrapper(*args, **kwargs):
        if user is None:
            return """
                <h3>You must log in<h3>
                <form action="/login_page" method="POST">
                <a href="/">Return to Login page</a>
                </form> 
            """
        else:
            return func(*args, **kwargs)

    return wrapper


@app.route("/")
@app.route("/login")
def login():
    return f"""
            <h3>Hello!<h3>
            <form action="/home_page" method="POST">
              <div>
                <label for="name">Please enter name</label>
                <input name ="name" id="add_name" />
              </div>
              <div>
                <label for="language">Please enter language</label>
                <input name ="lang" id="add_lang" />
              </div>
              <br>
                <button>Log in</button>
            </form>
            """


@app.route("/home_page", methods=["GET", "POST"])
#@is_login
def home_page():
    error_dict = {}
    name = validate_alfabet(request.form.get('name'), 'name', error_dict)
    language = request.form.get('lang')
    if error_dict:
        return f"""
                {error_dict['name']}
        """
    try:
        global user
        user = User(name, language)
        add_user = f"""
                INSERT INTO users VALUES ('{user.name}', '{user.language}', 'Default', '0')
        """
        cur.execute(add_user)
        con.commit()
        return f"""
            <h3>New user {user.name}, {user.language} was created!<h3>
            
            <form action="/add_grade" method="POST">
            <label for="grade">Please enter Grade</label>
                <button>Add grade</button>
            </form>
            """
    except:
        return f"""<h3>You entered invalid name or language<h3>
            <form action="/login_page" method="POST">
            <a href="/">Return to Login page</a>
            </form> 
            """


@app.route("/add_grade", methods=["GET", "POST"])
#@is_login
def get_grade():
    grade = randint(1, 13)
    user.grade = grade
    upd_user_grade = f"""
        UPDATE users SET grade = {user.grade} WHERE name IS '{user.name}';
    """
    save_data(upd_user_grade, "grade", grade)
    return f"""<h3>Grade for {user.name} is {user.grade}<h3>
            <form action="/add_course" method="POST">
            <label for="language">Please enter Course</label>
                <button>Add course</button>

        <br>
            </form>
            <form action="/login" method="POST">
            <a href="/login">Return to Login page</a>
            </form>
        """


@app.route("/add_course", methods=["GET", "POST"])
#@is_login
def get_course():
    return f"""<h3>Select Course for {user.name}<h3>
            <form action="/show_user_info" method="POST">
            <div>
                <input type="radio" name ="course" id="add_advanced" value="Advanced">
                <label for="course">Python Advanced</label>
            </div>
            <div>
                <input type="radio" name ="course" id="add_pro" value="Pro">
                <label for="course">Python Pro</label>
            </div>
            <div>
                <input type="radio" name ="course" id="add_basic" value="Basic">
                <label for="course">Python Basic</label>
            </div>
            <div>
                <input type="submit" value="Submit">
            </div>

            </form>
            <form action="/login" method="POST">
            <a href="/login">Return to Login page</a>
            </form>
            """


@app.route("/show_user_info", methods=["GET", "POST"])
#@is_login
def show_user_info():
    user.course = request.form.get('course')
    upd_user_course = f"""
            UPDATE users SET course = '{user.course}' WHERE name IS '{user.name}';
            """
    cur.execute(upd_user_course)
    con.commit()
    return f"<h3>User: {user.name}, {user.language} dev student on the course {user.course} got {user.grade} grade <h3>"


if __name__ == '__main__':
    con = sqlite3.connect('users.db', check_same_thread=False)
    cur = con.cursor()
    app.run(host='0.0.0.0', port=8000, debug=True)
