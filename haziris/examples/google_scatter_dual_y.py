import pandas as pd
import haziris as hz

df = pd.DataFrame([
    [0, 0, 67],
    [1, 1, 88],
    [2, 2, 77],
    [3, 3, 93],
    [4, 4, 85],
    [5, 5, 91],
    [6, 6, 71],
    [7, 7, 78],
    [8, 8, 93],
    [9, 9, 80],
    [10, 10, 82],
    [11, 0, 75],
    [12, 5, 80],
    [13, 3, 90],
    [14, 1, 72],
    [15, 5, 75],
    [16, 6, 68],
    [17, 7, 98],
    [18, 3, 82],
    [19, 9, 94],
    [20, 2, 79],
    [21, 2, 95],
    [22, 2, 86],
    [23, 3, 67],
    [24, 4, 60],
    [25, 2, 80],
    [26, 6, 92],
    [27, 2, 81],
    [28, 8, 79],
    [29, 9, 83]
  ],
  columns = ['Student ID', 'Hours Studied', 'Final']
)

options = {
    'series': {
      '0': {
        'targetAxisIndex': '0'
      },
      '1': {
        'targetAxisIndex': '1'
      }
    },
    'title': "Students Final Grades - based on hours studied",
    'vAxes': {
      '0': {
        'title': 'Hours Studied'
      },
      '1': {
        'title': 'Final Exam Grade'
      }
    }
  }

hz.google_scatter_chart( df, "google_scatter_dual_y.html", options )
