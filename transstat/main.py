from data_sources.dozor import get_vehicles
from data_sources.transphoto import get_records
from db import session
from db.models import City, Vehicle, Spot

cities = session.query(City).all()

for city in cities:
    records = get_records(city.trans_id, 1)
    print("TransPhoto data successfully fetched")

    db_vehicles = {
        v.number: v for v in
        session.query(Vehicle).filter(Vehicle.city_id == city.id).all()
    }

    for r in records.values():
        if r.number not in db_vehicles:
            print(f"<{city.name}> Adding new vehicle #{r.number}")
            session.add(
                Vehicle(number=r.number, city_id=city.id, model=r.model, type=const.TYPE.TRAM)
            )

    session.commit()
    db_vehicles = {
        v.number: v for v in
        session.query(Vehicle).filter(Vehicle.city_id == city.id).all()
    }

    spotted_vehicles = get_vehicles(city.dozor_id)

    data = {}
    for k in {*records, *spotted_vehicles}:
        data[k] = {'db': db_vehicles.get(k), 'tracking': spotted_vehicles.get(k)}

    missing = [d for d in data.values() if d['db'] is None]
    missing and print(f"WARNING: vehicles {', '.join(missing)} are absent in the DB")

    mapped_spots = [d for d in data.values() if d['db'] is not None and d['tracking'] is not None]

    for spot in mapped_spots:
        session.add(
            Spot(
                vehicle_id=spot['db'].id,
                city_id=city.id,
                trans_status=records[spot['db'].number].status
            )
        )

    session.commit()
