from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True)
    founded = db.Column(db.Integer, index=True)
    business = db.Column(db.String(256))
    revenue = db.Column(db.String(20))
    netincome = db.Column(db.String(20))
    equity = db.Column(db.String(20))
    debts = db.Column(db.String(20))
    bookvalue = db.Column(db.Integer, index=True)


db.create_all()


@app.route('/')
def index():
    users = User.query
    return render_template('basic_table.html', users=users)


if __name__ == '__main__':
    app.run()
