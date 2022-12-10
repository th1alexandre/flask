from uuid import uuid4

from sqlalchemy import Column, Integer, String
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import declarative_base

Base = declarative_base()


# SQLAlchemy table template
class TableA(Base):
    __tablename__ = "table_a"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    column_a = Column(String(100), nullable=False)
    column_b = Column(Integer, nullable=False)
