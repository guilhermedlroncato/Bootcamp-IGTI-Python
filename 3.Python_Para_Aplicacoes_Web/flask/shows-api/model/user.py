from data import alchemy

class UserModel(alchemy.Model):
    __tablename__ = 'user'

    id = alchemy.Column(alchemy.Integer, primary_key = True)
    username = alchemy.Column(alchemy.String(100), unique = True)
    password = alchemy.Column(alchemy.String(94))

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def json(self):
        return {'username': self.username, 'password': self.password}

    @classmethod
    def find_by_username(cls, username):
        return cls.query.filter.by(username = username).first()

    @classmethod
    def find_by_id(cls, id):
        return cls.query.filter.by(id = id).first()

    def save_to_db(self):
        alchemy.session.add(self)
        alchemy.session.commit()

    def delete_from_db(self):
        alchemy.session.delete(self)
        alchemy.session.commit()