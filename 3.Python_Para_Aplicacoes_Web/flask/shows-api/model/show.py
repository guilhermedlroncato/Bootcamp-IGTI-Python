from data import alchemy
from flask import Flask
from . import episode

class ShowModel(alchemy.Model):
    __tablename__ = 'shows'

    id = alchemy.Column(alchemy.Integer, primary_key = True)
    name = alchemy.Column(alchemy.String(80))

    episodes = alchemy.relationship(episode.EpisodeModel, lazy = 'dynamic')

    def __init__(self, name):
        self.name = name

    def json(self):
        return {
            'id': self.id,
            'name': self.name,
            'episodes' :[episode.json() for episode in self.episodes.all()]
        }

    def save_to_db(self):
        alchemy.session.add(self)
        alchemy.session.commit()

    def delete_from_db(self):
        alchemy.session.delete(self)
        alchemy.session.commit()

    def update_from_db(self):
        alchemy.session.update(self)
        alchemy.session.commit()

    @classmethod
    def find_by_name(cls, name):
        return cls.query.filter_by(name = name).first()

    @classmethod
    def find_by_id(cls, id):
        return cls.query.filter_by(id = id).first()