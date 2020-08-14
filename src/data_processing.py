import numpy as np
import pandas as pd
from copy import copy
import datetime

EUROPE = ['Albania', 'Andorra', 'Armenia', 'Austria', 'Azerbaijan', 'Belarus',
          'Belgium', 'Bosnia and Herzegovina', 'Bulgaria', 'Croatia', 'Cyprus',
          'Czechia', 'Denmark', 'Estonia', 'Finland', 'France', 'Georgia', 'Greece',
          'Hungary', 'Iceland', 'Ireland', 'Italy', 'Kazakhstan', 'Latvia',
          'Liechtenstein', 'Lithuania', 'Luxembourg', 'Malta', 'Moldova',
          'Monaco', 'Montenegro', 'Netherlands', 'North Macedonia', 'Norway',
          'Poland', 'Portugal', 'Romania', 'Russia', 'San Marino', 'Serbia',
          'Slovakia', 'Slovenia', 'Spain', 'Sweden', 'Switzerland', 'Turkey',
          'Ukraine', 'United Kingdom']


def prepare_europe_data(data, start_date, end_date, country=None):
    #get rid of unused columns
    df = data.copy()
    df = df.loc[df['Country/Region'].isin(EUROPE)]
    df = df[df['Province/State'].isna()]
    df = df.drop(['Province/State', 'Lat', 'Long'], axis=1)
    df = df.reset_index()
    df = df.drop(['index'], axis=1)
    #select given date range
    new_df = df['Country/Region']
    new_df = new_df.to_frame()
    new_df = new_df.join(df.loc[:, start_date:end_date])
    #select specified country
    if country:
        new_df = new_df.loc[new_df['Country/Region'] == country]
    return new_df


def prepare_empty_frame(start_date, end_date, country=None):
    #all european countries
    df = pd.DataFrame([country for country in EUROPE],
                      columns=['Country/Region'])
    #generate future dates
    dates = pd.date_range(start=start_date, end=end_date)
    list_of_dates = [date.strftime('%-m/%-d/%Y') for date in dates]
    #fill rows with 0
    for date in list_of_dates:
        df[date] = 0
    if country:
        df = df.loc[df['Country/Region'] == country]
    return df
