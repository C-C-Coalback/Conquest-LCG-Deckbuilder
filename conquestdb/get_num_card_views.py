import os
import pandas
import pandas as pd

cwd = os.getcwd()

if not os.path.exists(os.path.join(cwd, "card_views.csv")):
    df = pd.DataFrame({'name': [], 'count': []})
    df.to_csv(os.path.join(cwd, "card_views.csv"), index=False)

df = pd.read_csv(os.path.join(cwd, "card_views.csv"))

print(df['count'].sum())
