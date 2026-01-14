import os
import pandas
import pandas as pd

cwd = os.getcwd()

if not os.path.exists(os.path.join(cwd, "card_views.csv")):
    df = pd.DataFrame({'name': [], 'count': []})
    df.to_csv(os.path.join(cwd, "card_views.csv"), index=False)

df = pd.read_csv(os.path.join(cwd, "card_views.csv"))


def increment_card_count(card_name):
    global df
    if (df['name'] == card_name).any():
        df.loc[df['name'] == card_name, 'count'] += 1
    else:
        df.loc[-1] = [card_name, 1]  # adding a row
        df.index = df.index + 1  # shifting index
        df = df.sort_index()  # sorting by index
    df.to_csv(os.path.join(cwd, "card_views.csv"))
