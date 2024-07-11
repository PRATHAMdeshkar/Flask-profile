from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:password@localhost:5432/flask_database'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Task(db.Model):
    sno = db.Column(db.Integer, primary_key=True, autoincrement=True)
    YourName = db.Column(db.String(300), nullable=False)
    Email = db.Column(db.String(500), nullable=True)

with app.app_context():
    db.create_all()


@app.route("/", methods=['GET', 'POST'])
def emp():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']

        new_task = Task(YourName=name, Email=email)
        db.session.add(new_task)
        db.session.commit()
        return redirect(url_for('emp'))


        return render_template('index.html', tasks=tasks)
        tasks = Task.query.all()
    else:
        tasks = Task.query.all()
        return render_template('index.html', tasks=tasks)

if __name__ == "__main__":
    app.run(debug=True)
