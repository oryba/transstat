from bs4 import BeautifulSoup

from db.entity import TransRecord
from helpers import const
from helpers.req import http

status_mapping = {
    '1': const.STATUS.WORKING,
    '2': const.STATUS.NEW,
    '3': const.STATUS.IDLE
}


def get_records(city, _type) -> [TransRecord]:
    soup = BeautifulSoup(http.get(f'https://transphoto.org/list.php?t={_type}&cid={city}&st=0').text, 'html.parser')

    table = soup.findAll('div', {'class': 'p20w rtable'})[0]
    vehicles = table.findAll('tr')

    records = {}

    for vehicle in vehicles:
        number_a = vehicle.find('a')
        if not number_a:
            continue

        number = number_a.text
        idx = number_a.attrs['href']
        model = vehicle.find('td', {'class': 'cs'}).text
        status = status_mapping.get(vehicle.attrs['class'][0].replace('s', '')[-1])

        records[number] = TransRecord(number=number, model=model, status=status, _type=const.TYPE.TRAM)
    return records
