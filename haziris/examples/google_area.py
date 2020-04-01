import pandas as pd
import haziris as hz

df = pd.DataFrame({
  'Year'    : ['2013','2014','2015','2016'],
  'Sales'   : [1000  ,  1170,   660,  1030],
  'Expenses': [400   ,   460,  1120,   540]
})

hz.google_area_chart(df, "Google area.html")