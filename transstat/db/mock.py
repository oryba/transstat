from db import session
from db.models import City

cities = [
    City(name="Київ", dozor_id="", trans_id="96", kstat_id=""),
    City(name="Запоріжжя", dozor_id="zaporizhya", trans_id="147", kstat_id="zpstat"),
    City(name="Маріуполь", dozor_id="", trans_id="158", kstat_id="mstat"),
    City(name="КПТ", dozor_id="", trans_id="96", kstat_id="kpt"),
    City(name="Біла Церква", dozor_id="", trans_id="93", kstat_id="bcstat"),
    City(name="Житомир", dozor_id="", trans_id="137", kstat_id="ztstat"),
    City(name="Чернігів", dozor_id="", trans_id="116", kstat_id="cnstat"),
    City(name="Львів", dozor_id="", trans_id="10", kstat_id="lstat"),
    City(name="Тернопіль", dozor_id="", trans_id="119", kstat_id="tstat"),
    City(name="Чернівці", dozor_id="", trans_id="58", kstat_id="cvstat"),
    City(name="Івано-Франківськ", dozor_id="", trans_id="124", kstat_id="ifstat"),
    City(name="Хмельницький", dozor_id="", trans_id="132", kstat_id="khmstat"),
    City(name="Рівне", dozor_id="", trans_id="57", kstat_id="rvstat"),
    City(name="Луцьк", dozor_id="", trans_id="113", kstat_id="lustat"),
    City(name="Львівська обл.", dozor_id="", trans_id="", kstat_id="lostat"),
    City(name="Миколаїв", dozor_id="", trans_id="99", kstat_id="mkstat"),
    City(name="Одеса", dozor_id="", trans_id="23", kstat_id="odstat"),
    City(name="Херсон", dozor_id="", trans_id="115", kstat_id="khestat"),
    City(name="Кропивницький", dozor_id="", trans_id="247", kstat_id="krstat"),
    City(name="Кривий Ріг", dozor_id="", trans_id="67", kstat_id="krrstat"),
    City(name="Кам'янське", dozor_id="", trans_id="31", kstat_id="dzstat"),
    City(name="Дніпро", dozor_id="", trans_id="33", kstat_id="dpstat"),
    City(name="Краматорськ", dozor_id="", trans_id="157", kstat_id="krmstat"),
    City(name="Суми", dozor_id="", trans_id="194", kstat_id="sstat"),
    City(name="Полтава", dozor_id="", trans_id="168", kstat_id="pstat"),
    City(name="Кременчук", dozor_id="", trans_id="255", kstat_id="krestat"),
    City(name="Харків", dozor_id="", trans_id="101", kstat_id="khstat")
]

session.add_all(cities)
session.commit()
