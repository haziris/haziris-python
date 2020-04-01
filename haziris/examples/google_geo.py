import pandas as pd
import haziris as hz

df = pd.DataFrame([
          ['Germany'      , 200],
          ['United States', 300],
          ['Brazil'       , 400],
          ['Canada'       , 500],
          ['France'       , 600],
          ['RU'           , 700]
  ],
  columns = ['Country', 'Popularity']
)

hz.google_geo_chart(df, "Google geo.html")
