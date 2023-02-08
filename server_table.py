from flask import Flask, render_template, request
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
    return render_template('server_table.html')


@app.route('/api/data')
def data():
    query = User.query

    # search filter
    search = request.args.get('search')
    if search:
        query = query.filter(db.or_(
            User.name.like(f'%{search}%'),
            User.email.like(f'%{search}%')
        ))
    total = query.count()

    # sorting
    sort = request.args.get('sort')
    if sort:
        order = []
        for s in sort.split(','):
            direction = s[0]
            name = s[1:]
            if name not in ['name', 'age', 'email']:
                name = 'name'
            col = getattr(User, name)
            if direction == '-':
                col = col.desc()
            order.append(col)
        if order:
            query = query.order_by(*order)

    # pagination
    start = request.args.get('start', type=int, default=-1)
    length = request.args.get('length', type=int, default=-1)
    if start != -1 and length != -1:
        query = query.offset(start).limit(length)

    # response
    return {
        'data': [user.to_dict() for user in query],
        'total': total,
    }


if __name__ == '__main__':
    app.run()
