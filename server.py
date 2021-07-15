from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'app secret key'

@app.route('/')
def index():
    if "count" not in session:
        session["count"] = 1
    else:    
        session["count"] += 1
    
    return render_template("index.html")    

@app.route("/count", methods=["POST"])
def view_count():
    if request.form["alter"]=="reset":
        session["count"] = 0

    return redirect("/")

@app.route("/destroy")
def destroy():
    session.clear()
    return redirect("/")

if __name__=="__main__":
    app.run(debug=True)