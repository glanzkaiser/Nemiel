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

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'founded': self.founded,
            'business': self.business,
            'revenue': self.revenue,
            'netincome': self.netincome,
            'equity': self.equity,
            'debts': self.debts,
            'bookvalue': self.bookvalue
        }


db.create_all()

@app.route('/')
def index():
    return render_template('ajax_table.html')


@app.route('/api/data')
def data():
    return {'data': [user.to_dict() for user in User.query]}


if __name__ == '__main__':
    app.run()
