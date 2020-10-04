from server import *
from server.data_entry.db.add_notice import *


@app.route("/Data/Entry")
def data_entry_home():
    if "Data Entry" in session:
        return render_template("/data_entry/home.html")
    else:
        return abort(404)


@app.route("/Data/Entry/Notices",methods=['POST','GET'])
def new_notice():
    if "Data Entry" in session:
        if request.method == 'POST':
            title = request.form["T"]
            description = request.form["D"]
            add_notice(title=title, description=description)
            flash("New Notice Added ! ", "success")
            return redirect("/Data/Entry")
        else:
            return render_template("/data_entry/add_notice.html")
    else:
        return abort(404)