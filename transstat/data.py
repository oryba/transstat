from datetime import datetime
from functools import lru_cache

import pandas as pd

from db import session
from db.models import Vehicle, CountStat, City
from helpers import const


@lru_cache(maxsize=None)
def get_cities():
    return session.query(City).all()


@lru_cache(maxsize=None)
def get_service_count():
    data = session.query(CountStat).order_by(CountStat.date).all()

    df = pd.DataFrame({
        "Date": [datetime.fromordinal(d.date.toordinal()) for d in data],
        "Count": [d.count for d in data],
        "Type": [d.type for d in data],
        "City": [d.city_id for d in data]
    })

    df_weekends = df[df['Date'].dt.weekday >= 5]
    df_weekdays = df[df['Date'].dt.weekday <= 4]

    df_weekends_grouped = df_weekends.groupby(
        ['Type', 'City', pd.Grouper(key='Date', freq='W-MON')]
    )['Count'].mean().reset_index().sort_values('Date')
    df_weekends_grouped['day_type'] = "Weekend"

    df_weekdays_grouped = df_weekdays.groupby(
        ['Type', 'City', pd.Grouper(key='Date', freq='W-MON')]
    )['Count'].mean().reset_index().sort_values('Date')
    df_weekdays_grouped['day_type'] = "Weekday"

    df_weekly = pd.concat([df_weekdays_grouped, df_weekends_grouped]).sort_values(["Date", "Type"])
    df_weekly['Type'] = df_weekly['Type'] + ' ' + df_weekly['day_type']

    return df, df_weekly


@lru_cache(maxsize=None)
def get_count_data(city_id, count_options):
    df, df_weekly = get_service_count()
    target_df = df_weekly if 'group_by_weeks' in count_options else df
    return target_df[target_df["City"] == city_id]


@lru_cache(maxsize=None)
def get_model_stats(city_id, model_options):
    data = Vehicle.vehicles_status_by_city(city_id)
    df_vehicles = pd.DataFrame(data)
    df_vehicles.columns = data.keys()

    target_df = df_vehicles[
        df_vehicles['status'] == const.STATUS.WORKING] if "working_only" in model_options else df_vehicles
    target_df = target_df[target_df['purpose'] == 'Pass'] if "include_serv" not in model_options else target_df

    return target_df.value_counts(subset=['model', 'type']).rename_axis(
        ['model', 'type']).reset_index(name='count')
