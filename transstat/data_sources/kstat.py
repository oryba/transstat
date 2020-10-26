import re
from datetime import timedelta, date

from bs4 import BeautifulSoup

from db import session
from db.models import CountStat, City
from helpers import const
from helpers.req import http

kind_mapping = {
    "трам": const.TYPE.TRAM,
    "трол": const.TYPE.TROLL
}


def date_range(start_date, end_date):
    for n in range(int((end_date - start_date).days)):
        yield start_date + timedelta(n)


def get_counts_by_date(city, date_repr: str):
    result = {const.TYPE.TRAM: 0, const.TYPE.TROLL: 0}
    soup = BeautifulSoup(http.get(f'http://kstat.pp.ua/{city}/?action=list&date={date_repr}').text, 'html.parser')
    for rec in re.findall(
            r'(?P<count>\d+) (?P<kind>.+?) ',
            str(soup(text=re.compile(r'В цей день зафіксовано'))[0])
    ):
        trim_kind = rec[1][:4]
        if trim_kind in kind_mapping:
            result[kind_mapping[trim_kind]] = int(rec[0])

    return result


def update_city_data(city: City):
    start_date = date(2014, 10, 1)
    end_date = date.today() - timedelta(1)

    existing_stats = {
        s.date: s for s in
        session.query(CountStat).filter(CountStat.city_id == city.id, CountStat.date.between(start_date, end_date)).order_by(CountStat.date).all()
    }

    for single_date in date_range(start_date, end_date):
        str_date = single_date.strftime("%Y-%m-%d")
        if single_date not in existing_stats:
            print(f"<{city.name}> Requesting KStat for date {str_date}")
            rec = get_counts_by_date(city.kstat_id, date_repr=str_date)
            for k, v in rec.items():
                session.add(CountStat(type=k, count=v, date=single_date, city_id=city.id))

    session.commit()


def update_data():
    cities = session.query(City).all()
    for city in cities:
        update_city_data(city)