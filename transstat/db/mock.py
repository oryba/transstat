from db import session
from db.models import City

cities = [
    City(name="Київ", dozor_id="", trans_id="96", kstat_id=""),
    City(name="Запоріжжя", dozor_id="zaporizhya", trans_id="147", kstat_id="zpstat"),
    City(name="Маріуполь", dozor_id="", trans_id="158", kstat_id="mstat"),
    City(name="КПТ", dozor_id="", trans_id="96", kstat_id="kpt"),
    City(name="Біла Церква", dozor_id="", trans_id="", kstat_id="bcstat"),
    City(name="Житомир", dozor_id="", trans_id="", kstat_id="ztstat"),
    City(name="Чернігів", dozor_id="", trans_id="", kstat_id="cnstat"),
    City(name="Львів", dozor_id="", trans_id="", kstat_id="lstat"),
    City(name="Тернопіль", dozor_id="", trans_id="", kstat_id="tstat"),
    City(name="Чернівці", dozor_id="", trans_id="", kstat_id="cvstat"),
    City(name="Івано-Франківськ", dozor_id="", trans_id="", kstat_id="ifstat"),
    City(name="Хмельницький", dozor_id="", trans_id="", kstat_id="khmstat"),
    City(name="Рівне", dozor_id="", trans_id="", kstat_id="rvstat"),
    City(name="Луцьк", dozor_id="", trans_id="", kstat_id="lustat"),
    City(name="Львівська обл.", dozor_id="", trans_id="", kstat_id="lostat"),
    City(name="Миколаїв", dozor_id="", trans_id="", kstat_id="mkstat"),
    City(name="Одеса", dozor_id="", trans_id="", kstat_id="odstat"),
    City(name="Херсон", dozor_id="", trans_id="", kstat_id="khestat"),
    City(name="Кропивницький", dozor_id="", trans_id="", kstat_id="krstat"),
    City(name="Кривий Ріг", dozor_id="", trans_id="", kstat_id="krrstat"),
    City(name="Кам'янське", dozor_id="", trans_id="", kstat_id="dzstat"),
    City(name="Дніпро", dozor_id="", trans_id="", kstat_id="dpstat"),
    City(name="Краматорськ", dozor_id="", trans_id="", kstat_id="krmstat"),
    City(name="Суми", dozor_id="", trans_id="", kstat_id="sstat"),
    City(name="Полтава", dozor_id="", trans_id="", kstat_id="pstat"),
    City(name="Кременчук", dozor_id="", trans_id="", kstat_id="krestat"),
    City(name="Харків", dozor_id="", trans_id="", kstat_id="khstat")
]

session.add_all(cities)
session.commit()
