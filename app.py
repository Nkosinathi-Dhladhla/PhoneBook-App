from flask import Flask, render_template, redirect, request
from flask_sqlalchemy import SQLAlchemy

#My app:
app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
db = SQLAlchemy(app)

class MyContacts(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(100), nullable = False)
    email = db.Column(db.String(100))
    phone = db.Column(db.String(20), nullable = False)

    def __repr__(self):
        return f"<Contact{self.id} - {self.name}>"

@app.route("/add", methods=["GET", "POST"])
def add_contact():
    if request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email")
        phone = request.form.get("phone")

        new_contact = MyContacts(name=name, email=email, phone=phone)
        
        try:
            db.session.add(new_contact)
            db.session.commit()
            return redirect("/")
        except Exception as e:
            return f"ERROR: {e}"
    return render_template("add.html")

@app.route("/edit/<int:id>", methods = ["GET", "POST"])
def edit_contact(id:int):
    contact = MyContacts.query.get_or_404(id)
    if request.method == "POST":
        contact.name = request.form['name']
        contact.email = request.form['email']
        contact.phone = request.form['phone']

        try:
            db.session.commit()
            return redirect("/")
        except Exception as e:
            return f"Error: {e}"
    else:
        return render_template('edit.html', contact=contact)


@app.route("/delete/<int:id>")
def delete_contact(id:int):
    delete_contact = MyContacts.query.get_or_404(id)
    try:
        db.session.delete(delete_contact)
        db.session.commit()
        return redirect("/")
    except Exception as e:
        return f"ERROR: {e}"


@app.route("/")
def index():
    contacts = MyContacts.query.all()
    return render_template("index.html", contacts=contacts)


if __name__ == ("__main__"):
    with app.app_context():
        db.create_all()

    app.run(debug=True)