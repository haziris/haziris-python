import pandas as pd
import haziris as hz

df = pd.DataFrame({
  'Element' : ['Copper','Silver','Gold','Platinum'],
  'Density' : [    8.94,   10.49, 19.30,     21.45]
})

hz.google_column_chart(df, "google_column.html", {'legned':'None'})
