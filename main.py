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
            <h3>Hello {user.name}!<h3>
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
            <form action="/show_user_info" method="POST">
            <div>
                <input type="radio" name ="course" id="add_advanced" value="Python Advanced">
                <label for="course">Python Advanced</label>
            </div>
            <div>
                <input type="radio" name ="course" id="add_pro" value="Python Pro">
                <label for="course">Python Pro</label>
            </div>
            <div>
                <input type="radio" name ="course" id="add_basic" value="Python Basic">
                <label for="course">Python Basic</label>
            </div>
            <div>
                <input type="submit" value="Submit">
            </div>

            <br>
            <a href="/show_user_info">Return to Home page</a>
            </form>
            """


@app.route("/add_grade", methods=["GET", "POST"])
def get_grade():
    grade = randint(1, 13)
    user.grade = grade
    return f"""<h3>Grade for  {user.name} is {user.grade}<h3>
            <form action="/show_user_info" method="POST">
            <a href="/">Return to Home page</a>
        <br>
            <a href="/show_user_info">Show information about User</a>
            </form>
    """


@app.route("/show_user_info", methods=["GET", "POST"])
def show_user_info():
    user.course = request.form.get('course')
    return f"<h3>User: {user.name}, {user.language} dev student on the course {user.course} got {user.grade} grade <h3>" \
           f"<h3>{request.form.get('course')}<h3>"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)
