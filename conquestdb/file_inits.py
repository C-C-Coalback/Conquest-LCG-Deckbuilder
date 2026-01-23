import os
import pandas
import pandas as pd
import datetime

cwd = os.getcwd()

if not os.path.exists(os.path.join(cwd, "card_views.csv")):
    df = pd.DataFrame({'name': [], 'count': []})
    df.to_csv(os.path.join(cwd, "card_views.csv"))

if not os.path.exists(os.path.join(cwd, "views_dates.csv")):
    dates_df = pd.DataFrame({'date': [], 'count': []})
    dates_df.to_csv(os.path.join(cwd, "views_dates.csv"))

df = pd.read_csv(os.path.join(cwd, "card_views.csv"), index_col=0)
dates_df = pd.read_csv(os.path.join(cwd, "views_dates.csv"), index_col=0)


def increment_date_csv_count():
    global dates_df
    date_current = datetime.date.today().strftime("%Y-%m-%d")
    if (dates_df['date'] == date_current).any():
        dates_df.loc[dates_df['date'] == date_current, 'count'] += 1
    else:
        dates_df.loc[-1] = [date_current, 1]
        dates_df.index = dates_df.index + 1
        dates_df = dates_df.sort_index()
    dates_df.to_csv(os.path.join(cwd, "views_dates.csv"))


def increment_card_count(card_name):
    global df
    if (df['name'] == card_name).any():
        df.loc[df['name'] == card_name, 'count'] += 1
    else:
        df.loc[-1] = [card_name, 1]  # adding a row
        df.index = df.index + 1  # shifting index
        df = df.sort_index()  # sorting by index
    df.to_csv(os.path.join(cwd, "card_views.csv"))
