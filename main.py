from flask import Flask, request
from random import randint

app = Flask(__name__)


class User:

    def __init__(self, name='', language=''):
        self.grade = ''
        self.course = ''
        self.name = name
        self.language = language

    @app.route("/login")
    def login(self):
        languages = {'Python', 'Java', 'JS', 'Ruby'}

        name = input()
        language = input()
        if name.isalpha() and language in languages:
            return f"""
            <h3>Hello!<h3>
            <form action="/add_course" method="POST">
              <div>
                <label for="course">Please enter course</label>
                <input name ="course" id="add_course" value="str" />
              </div>
                <button>Add course</button>
            </form> """
        else:
            if language not in languages:
                return f'<h3>You chose incorrect language. Try again!<h3>'
            else:
                return f"<h3>Name can't contain digits or symbols<h3>"

    @app.route("/add_course", methods=["POST"])
    def get_course(self):
        courses = {'Basic', 'Pro', 'Advanced'}
        course = input()
        if course not in courses:
            return f"<h3>Sorry! You can select course only from list<h3>"
        else:
            self.course = course
            return f"""<h3>Course for {self.name} is {self.course}<h3>
            <a href="/">Return to Home page</a>
            """

    @app.route("/add_grade", methods=["POST"])
    def get_grade(self):
        grade = randint(1, 13)
        self.grade = grade
        return f"""<h3>Grade for {self.name} is {self.grade}<h3>
                <a href="/">Return to Home page</a>
        """


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)
    user1 = User("Alisa", "Python")
