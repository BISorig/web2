from sqlalchemy import orm
import sqlalchemy.ext.declarative
from .db_session import SqlAlchemyBase


class Departament(SqlAlchemyBase):
    __tablename__ = 'departament'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    title = sqlalchemy.Column(sqlalchemy.String)
    chief = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey('users.id'))
    members = sqlalchemy.Column(sqlalchemy.String)
    email = sqlalchemy.Column(sqlalchemy.String)
    user = orm.relationship('User')