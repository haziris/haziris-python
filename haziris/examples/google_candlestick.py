import pandas as pd
import haziris as hz

df = pd.DataFrame([
    ['Mon', 20, 28, 38, 45],
    ['Tue', 31, 38, 55, 66],
    ['Wed', 50, 55, 77, 80],
    ['Thu', 77, 77, 66, 50],
    ['Fri', 68, 66, 22, 15]
  ],
  columns = ['Day', 'min', 'start', 'end', 'max']
)

hz.google_candlestick_chart( df, "Google candlestick.html", {'legend': 'none'} )
