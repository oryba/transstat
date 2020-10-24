import time

from db.entity import Route, Vehicle
from helpers import const
from helpers.req import http

routes_mapping = {
    '{3}': const.TYPE.TRAM,
    # '{2}': const.TYPE.TROLL
}


def get_by_route(r: int, _type: str, cookies: dict):
    print(f"Getting vehicles for route #{r}")
    response = http.get(
        'https://city.dozor.tech/data',
        params={
            't': '2',
            'p': str(r)
        },
        cookies=cookies
    ).json()

    time.sleep(0.3)

    if not response['data']:
        return []

    return [Vehicle(idx=v['id'], _type=_type, number=v['gNb'].replace('Т-', '')) for v in response['data'][0]['dvs']]


def get_vehicles(city_name):
    cookies = {
        'gts.web.uuid': '9806D2D8-9680-4A82-80AB-9FCEA8FE6780',
        'gts.web.city': city_name
    }

    routes_data = http.get('https://city.dozor.tech/data?t=1', cookies=cookies)

    routes = []

    for route in routes_data.json()['data']:
        if route['inf'] in routes_mapping:
            vehicles = get_by_route(route['id'], route['inf'], cookies)
            routes.append(Route(
                idx=route['id'],
                _type=routes_mapping[route['inf']],
                name=route['sNm'],
                vehicles=vehicles
            ))

    vehicles_registry = {}

    for r in routes:
        for v in r.vehicles:
            vehicles_registry[v.number] = v

    return vehicles_registry
