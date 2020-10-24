import datetime

from sqlalchemy import Column, Integer, String, ForeignKey, DateTime

from db import Base, engine


class City(Base):
    __tablename__ = 'cities'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    trans_id = Column(String)
    dozor_id = Column(String)
    created_time = Column(DateTime, default=datetime.datetime.utcnow)

    def __repr__(self):
        return f"<City {self.name}>"


class Vehicle(Base):
    __tablename__ = 'vehicles'

    id = Column(Integer, primary_key=True, autoincrement=True)
    city_id = Column(Integer, ForeignKey('cities.id'))
    number = Column(String)
    model = Column(String)
    type = Column(String)
    dozor_id = Column(String, default=None)
    created_time = Column(DateTime, default=datetime.datetime.utcnow)

    def __repr__(self):
        return f"<Vehicle {self.model} #{self.number}>"


class Spot(Base):
    __tablename__ = 'spots'

    id = Column(Integer, primary_key=True, autoincrement=True)
    vehicle_id = Column(Integer, ForeignKey('vehicles.id'))
    city_id = Column(Integer, ForeignKey('cities.id'))
    trans_status = Column(String)
    spotted_time = Column(DateTime, default=datetime.datetime.utcnow)

    def __repr__(self):
        return f"<Spotted vehicle {self.vehicle_id} in city {self.city_id}>"


Base.metadata.create_all(engine)
