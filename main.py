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
        return f"""
            <h3>Hello!<h3>
            <form action="/add_course" method="POST">
            <label for="language">Please enter Course</label>
                <button>Add course</button>
            </form>
            <form action="/add_grade" method="POST">
            <label for="language">Please enter Grade</label>
                <button>Add grade</button>
            </form>
        """
    except:
        return f"""<h3>You entered invalid name or language<h3>
            <form action="/home_page" method="POST">
            <a href="/">Return to Login page</a>
            </form> 
            """


@app.route("/add_course", methods=["POST"])
def get_course():
    return f"""<h3>Course for is <h3>
            <form action="/home_page" method="POST">
            <div>
                <input type="radio" name ="advanced" id="add_advanced" value="str">
                <label for="language">Python Advanced</label>
            </div>
            <div>
                <input type="radio" name ="Pro" id="add_pro" value="str">
                <label for="language">Python Pro</label>
            </div>
            <div>
                <input type="radio" name ="basic" id="add_basic" value="str">
                <label for="language">Python Basic</label>
            </div>

            <br>
            <a href="/home_page">Return to Home page</a>
            </form>
            """


@app.route("/add_grade", methods=["POST"])
def get_grade():
    grade = randint(1, 13)
    return f"""<h3>Grade for  is {grade}<h3>
             <a href="/">Return to Home page</a>
    """


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)

