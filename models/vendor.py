from sqlalchemy import Column, Integer, String

from config.sqlite_config import Base


class Vendor(Base):
    __tablename__ = 'vendors'

    id = Column(Integer, primary_key=True, autoincrement=True)
    vendor_name = Column(String, nullable=False, unique=True)
    base_url = Column(String, nullable=False)