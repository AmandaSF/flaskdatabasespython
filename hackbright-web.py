from flask import Flask, request, render_template

import hackbright

app = Flask(__name__)

@app.route("/student")
def get_student():
    """Show information about a student."""

    github = request.args.get('github','jhacks')
    first, last, github = hackbright.get_student_by_github(github)
    html = render_template('student_info.html', first=first, last=last, github=github)
    return html

@app.route("/student-search")
def get_student_form():
    """Show form for searching for a student."""

    return render_template("student_search.html")

@app.route("/add-student", methods=['POST'])
def add_student():
    """Adds new student to database"""
    first_name = request.form.get('first_name')
    last_name = request.form.get('last_name')
    github = request.form.get('github')
    hackbright.make_new_student(first_name=first_name,last_name=last_name, github=github)
    html = render_template('student_info.html', first=first_name, last=last_name, github=github)
    return html
    

@app.route("/student-add") 
def student_add():
    """ Show add student form."""
    return render_template("student-add.html")   

if __name__ == "__main__":
    app.run(debug=True)