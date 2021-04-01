import datetime
import sqlalchemy
from .db_session import SqlAlchemyBase
from sqlalchemy import orm

from .users import User


class Jobs(SqlAlchemyBase):
    __tablename__ = 'jobs'
    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    team_leader = sqlalchemy.Column(
        sqlalchemy.Integer, sqlalchemy.ForeignKey("users.id"), autoincrement=True)
    job = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    work_size = sqlalchemy.Column(sqlalchemy.Integer, nullable=True)
    collaborators = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    start_date = sqlalchemy.Column(
        sqlalchemy.DateTime, default=datetime.datetime.now)
    end_date = sqlalchemy.Column(
        sqlalchemy.DateTime, default=datetime.datetime.now)
    is_finished = sqlalchemy.Column(
        sqlalchemy.Boolean, nullable=True
    )

    user = orm.relation("User")

    def __repr__(self):
        return f'{self.id} {self.team_leader} {self.job} {self.work_size}' \
               f' {self.collaborators} {self.start_date} {self.end_date} ' \
               f'{self.is_finished}'
