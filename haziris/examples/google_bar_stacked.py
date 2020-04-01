import pandas as pd
import haziris as hz

df = pd.DataFrame({
  'Genre'            : ['2010','2020','2030'],
  'Fantasy & Sci Fi' : [    10,    16,    28],
  'Romance'          : [    24,    22,    19],
  'Mystery/Crime'    : [    20,    23,    29]
})

hz.google_bar_chart(df, "Google bar - stacked.html", {'isStacked': True})
