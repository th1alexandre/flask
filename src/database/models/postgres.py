from datetime import datetime as dt
from uuid import uuid4

from sqlalchemy import Column, Integer, String
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import declarative_base

from database.postgres import db

Base = declarative_base()


# Pure SQLAlchemy template
class TableA(Base):
    __tablename__ = "table_a"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    column_a = Column(String(100), nullable=False)
    column_b = Column(Integer, nullable=False)


# Flask-SQLAlchemy template
class TableB(db.Model):
    __tablename__ = "table_b"
    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    column_a = db.Column(db.Boolean, unique=False)
    column_b = db.Column(db.DateTime, unique=True, default=dt.utcnow)
