from server import *
from server.teacher.db.add import *


@app.route("/Teacher/")
def teacher_temporary_home():
    if "Teacher" in session:
        return render_template("/teacher/home.html")
    return abort(404)


@app.route("/Teacher/Add")
def add():
    if "Teacher" in session:
        return render_template("/teacher/add.html")
    return abort(404)


@app.route("/Teacher/Logout")
def teacher_logout():
    if "Teacher" in session:
        session.pop("Teacher", None)
        return redirect("/")
    return abort(404)


@app.route("/Teacher/Add/Student", methods=["POST", "GET"])
def add_student():
    if "Teacher" in session:
        if request.method == "POST":
            user_name = request.form["UN"]
            email = request.form["E"]
            passwrod = request.form["P"]
            add_s = Add_Student(user_name=user_name, passwrod=passwrod, email=email)
            result = add_s.add_to_db()
            if result[0] is True:
                flash(result[1], "success")
                return redirect("/Teacher/")
            else:
                for x in result[1]:
                    flash(x, "danger")
                return redirect("/Teacher/Add/Student")
        else:
            return render_template("/teacher/add_students.html")
    return abort(404)


@app.route("/Teacher/Add/Data/Entry", methods=["POST", "GET"])
def add_data_entry():
    if "Teacher" in session:
        if request.method == "POST":
            user_name = request.form["UN"]
            email = request.form["E"]
            passwrod = request.form["P"]
            add_de = Add_Data_Entry(user_name=user_name, passwrod=passwrod, email=email)
            result = add_de.add_to_db()
            if result[0] is True:
                flash(result[1], "success")
                return redirect("/Teacher/")
            else:
                for x in result[1]:
                    flash(x, "danger")
                return redirect("/Teacher/Add/Data/Entry")
        else:
            return render_template("/teacher/add_data_entry.html")
    return abort(404)