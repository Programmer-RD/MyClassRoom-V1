from server import *
from server.sys.db.auth import *


@app.route("/", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        user_name_or_email = request.form["EOUN"]
        password = request.form["P"]
        role = request.form["R"]
        if (
            role == "Teacher"
            and user_name_or_email == "go2ranuga@gmail.com"
            or user_name_or_email == "RANUGA"
            and password == "RANUGA"
        ):
            session["Teacher"] = True
            return redirect("/Teacher")
        si = Sign_In(
            role=role, user_name_or_email=user_name_or_email, passwrod=password
        )
        result = si.check()
        if result is True:
            if role == "Student":
                session["Student"] = True
                return redirect("/Student")
            elif role == "Data Entry":
                session["Data Entry"] = True
                return redirect("/Data/Entry")
        return "False"
    else:
        return render_template("/sys/login.html")
