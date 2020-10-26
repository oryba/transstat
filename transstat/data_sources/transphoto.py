from bs4 import BeautifulSoup

from db import session
from db.entity import TransRecord
from db.models import City, Vehicle, Spot
from helpers import const
from helpers.req import http

status_mapping = {
    '1': const.STATUS.WORKING,
    '2': const.STATUS.NEW,
    '3': const.STATUS.IDLE
}

types_mapping = {
    const.TYPE.TRAM: 1,
    const.TYPE.TROLL: 2
}

serv_mapping = {
    0: "Pass",
    1: "Serv",
    2: "Mus"
}


def get_records_by_city(city, _type) -> [TransRecord]:
    records = {}

    for serv in serv_mapping:
        soup = BeautifulSoup(http.get(f'https://transphoto.org/list.php?t={_type}&cid={city}&st=0&serv={serv}').text,
                             'html.parser')

        table = soup.find('div', {'class': 'p20w rtable'})
        if not table:
            continue
        vehicles = table.findAll('tr')

        for vehicle in vehicles:
            number_a = vehicle.find('a')
            if not number_a:
                continue

            number = number_a.text
            idx = number_a.attrs['href']
            model = vehicle.find('td', {'class': 'cs'}).text
            status = status_mapping.get(vehicle.attrs['class'][0].replace('s', '')[-1])

            records[number] = TransRecord(number=number, model=model, status=status, _type=const.TYPE.TRAM,
                                          purpose=serv_mapping[serv])
    return records


def get_records():
    cities = session.query(City).filter(City.trans_id != '').all()
    for city in cities:
        print(f"<{city.name}> Fetching TransPhoto data")
        # TODO: replace with a single query
        vehicles = {(v.number, v.type): v for v in session.query(Vehicle).filter(City.id == city.id).all()}

        spotted = {}
        for _type in const.TYPE.values():
            for num, rec in get_records_by_city(city.trans_id, types_mapping[_type]).items():
                key = (num, _type)
                if key not in vehicles:
                    veh = Vehicle(
                        number=num,
                        city_id=city.id,
                        model=rec.model,
                        type=_type
                    )
                    vehicles[key] = veh
                else:
                    veh = vehicles[key]
                session.add(veh)
                spotted[key] = rec
            session.flush()

            for veh in vehicles.values():
                rec = spotted.get((veh.number, veh.type))
                session.add(Spot(
                    vehicle_id=veh.id,
                    city_id=city.id,
                    trans_status=rec.status if rec else 'Unknown',
                    purpose=rec.purpose if rec else 'Unknown'
                ))
        session.commit()
