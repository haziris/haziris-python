import pandas as pd
import haziris as hz
import numpy as np

df = pd.DataFrame({
  'Name': [str(x) for x in range(5)],
  'a': np.random.rand(5), 
  'b': np.random.rand(5), 
  'c': np.random.rand(5), 
  'd': np.random.rand(5) 
})

hz.google_bar_chart(df, "Google bar 1.html")
