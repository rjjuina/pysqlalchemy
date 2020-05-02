from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()

class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)
    address = Column(String)
    email = Column(String)

    def __repr__(self):
        return "<User(id='%s', name='%s', age='%s', address='%s', email='%s')>" % (
            self.id, self.name, self.age, self.address, self.email)