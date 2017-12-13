# coding=utf-8
from app import db

ROLE_USER = 0
ROLE_ADMIN = 1


class Team(db.Model):
    __tablename__ = 'Team'
    id = db.Column('id', db.Integer, primary_key=True, autoincrement=True)
    members = db.Column('members', db.Integer)
    member = db.relationship("User", backref = "team")

    def __getitem__(self, item):
        return self.id

    def __init__(self, members):
        self.members = members

class User(db.Model):
    __tablename__ = 'User'
    id = db.Column('id', db.Integer, primary_key= True, autoincrement = True)
    email = db.Column('email', db.String(140))
    nickname = db.Column('nickname', db.String(60))
    password = db.Column('password', db.String(60))
    team_id = db.Column('team_id', db.Integer, db.ForeignKey(Team.id))
    #role = db.Column('role', db.Integer)

    def __getitem__(self, item):
        if item == 'password':
            return self.password

    def __init__(self, password, nickname, email):
        self.email = email
        self.password = password
        self.nickname = nickname
        #self.role = role
