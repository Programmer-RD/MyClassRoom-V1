from server import *
from server.student.db.get_notices import *


@app.route("/Student/")
@app.route("/Student")
def student_home():
    if "Student" in session:
        return render_template("/student/home.html")
    else:
        return abort(404)


@app.route("/Student/Chat")
def student_chat():
    if "Student" in session:
        return render_template("/student/chat.html")
    else:
        return abort(404)


@app.route("/Student/Logout")
def student_logout():
    if "Student" in session:
        session.pop("Student", None)
        return redirect("/")
    else:
        return abort(404)


@app.route("/Student/Notices/")
def student_notices():
    if "Student" in session:
        notices = get_notices()
        return render_template("/student/notices.html", notices=notices)
    else:
        return abort(404)


@app.route("/Student/Docs")
def student_docs():
    if "Student" in session:
        return render_template("/student/docs.html")
    else:
        return abort(404)


@app.route("/Student/Contact")
def contact():
    return render_template("/student/contact.html")
