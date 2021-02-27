from flask import Flask, render_template, url_for, request, redirect
import csv
app=Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

def write_to_csv(data):
    with open("database.csv", newline="\n", mode="a") as database:
        email = data["email"]
        name = data["name"]
        message = data["message"]
        csv_writter = csv.writer(
            database, delimiter=",", quotechar="'", quoting=csv.QUOTE_MINIMAL
        )
        csv_writter.writerow([name, email, message])

@app.route("/submit_form",methods=["POST","GET"])
def message():
        if request.method=="POST":
            data=request.form.to_dict()
            name=data["name"]
            write_to_csv(data)
            return (f"thank you {name} for contacting us")
