from db import session
from db.models import City

cities = [
    City(name="Запоріжжя", dozor_id="zaporizhya", trans_id="147")
]

session.add_all(cities)
session.commit()
