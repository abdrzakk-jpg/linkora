
from app.db.database import Base
from sqlalchemy import (
    Boolean,
    Column,
    String,
    Index,
    false
)


class Url(Base):
    """ URL model in DB"""
    
    __tablename__ = 'urls'
    
    id = Column(String(10), primary_key=True, nullable=False, unique=True)
    long_url = Column(String, primary_key=True, nullable=False, unique=True)
    valid = Column(Boolean, default=false(), nullable=False) # True/False, depends on url reachability
    
    __table_args__ = (
        Index("long_url_idx", "long_url"),
    )