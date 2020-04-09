import pandas as pd
import haziris as hz
import numpy as np

df = pd.DataFrame([
            [22, np.nan, 12],
            [ 7, np.nan, 40],
            [14, np.nan, 31],
            [37, np.nan, 30],
            [18, np.nan, 17],
            [ 9, np.nan, 20],
            [26, np.nan, 36],
            [ 5, np.nan, 13],
            [36, np.nan, 30],
            [35, np.nan, 15],
            [24, np.nan, 12],
            [ 7, np.nan, 31],
            [10, np.nan, 12],
            [24, np.nan, 40],
            [37, np.nan, 18],
            [32, np.nan, 21],
            [35, np.nan,  7],
            [31, np.nan, 30],
            [21, np.nan, 42],
            [12, np.nan, 10],
            [10, 13, np.nan],
            [40, 12, np.nan],
            [28, 29, np.nan],
            [32, 22, np.nan],
            [31, 37, np.nan],
            [38,  5, np.nan],
            [ 6,  4, np.nan],
            [21, 36, np.nan],
            [22,  8, np.nan],
            [21, 22, np.nan],
            [28, 17, np.nan],
            [12,  5, np.nan],
            [37, 30, np.nan],
            [41,  7, np.nan],
            [41, 27, np.nan],
            [15, 20, np.nan],
            [14, 36, np.nan],
            [42,  3, np.nan],
            [14, 37, np.nan],
            [15, 36, np.nan]
  ],
  columns = ['', 'Medicine 1', 'Medicine 2']
)
previous = pd.DataFrame([
            [23, np.nan, 12],
            [ 9, np.nan, 39],
            [15, np.nan, 28],
            [37, np.nan, 30],
            [21, np.nan, 14],
            [12, np.nan, 18],
            [29, np.nan, 34],
            [ 8, np.nan, 12],
            [38, np.nan, 28],
            [35, np.nan, 12],
            [26, np.nan, 10],
            [10, np.nan, 29],
            [11, np.nan, 10],
            [27, np.nan, 38],
            [39, np.nan, 17],
            [34, np.nan, 20],
            [38, np.nan,  5],
            [33, np.nan, 27],
            [23, np.nan, 39],
            [12, np.nan, 10],
            [ 8, 15, np.nan],
            [39, 15, np.nan],
            [27, 31, np.nan],
            [30, 24, np.nan],
            [31, 39, np.nan],
            [35,  6, np.nan],
            [ 5,  5, np.nan],
            [19, 39, np.nan],
            [22,  8, np.nan],
            [19, 23, np.nan],
            [27, 20, np.nan],
            [11,  6, np.nan],
            [34, 33, np.nan],
            [38,  8, np.nan],
            [39, 29, np.nan],
            [13, 23, np.nan],
            [13, 36, np.nan],
            [39,  6, np.nan],
            [14, 37, np.nan],
            [13, 39, np.nan]
  ],
  columns = ['', 'Medicine 1', 'Medicine 2']
)

hz.google_scatter_chart( df, "google_scatter_diff.html", previous=previous )
