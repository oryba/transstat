import datetime

from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Date

from db import Base, engine, session


class City(Base):
    __tablename__ = 'cities'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    trans_id = Column(String)
    dozor_id = Column(String)
    kstat_id = Column(String)
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

    @classmethod
    def vehicles_status_by_city(cls, city_id: str):
        return engine.execute(f"""
            select *,
           (select s.purpose
            from spots s
            where v.id = s.vehicle_id and s.city_id = {city_id}
            order by s.spotted_time desc
            limit 1) as purpose,
           (select s.trans_status
            from spots s
            where v.id = s.vehicle_id and s.city_id = {city_id}
            order by s.spotted_time desc
            limit 1) as status
        from vehicles v
        where city_id = {city_id}
        """)


class Spot(Base):
    __tablename__ = 'spots'

    id = Column(Integer, primary_key=True, autoincrement=True)
    vehicle_id = Column(Integer, ForeignKey('vehicles.id'))
    city_id = Column(Integer, ForeignKey('cities.id'))
    trans_status = Column(String)
    purpose = Column(String)
    spotted_time = Column(DateTime, default=datetime.datetime.utcnow)

    def __repr__(self):
        return f"<Spotted vehicle {self.vehicle_id} in city {self.city_id}>"


class CountStat(Base):
    __tablename__ = 'count_stats'

    id = Column(Integer, primary_key=True, autoincrement=True)
    city_id = Column(Integer, ForeignKey('cities.id'))
    date = Column(Date)
    type = Column(String)
    count = Column(Integer)

    def __repr__(self):
        return f"<Spotted vehicles number on {self.date.strftime('%Y-%m-%d')}>"


Base.metadata.create_all(engine)
