# haziris
Visualizations for Python

- [Wiki](https://github.com/haziris/wiki)

## Installation
Binary installers for the latest released version are available at the [Python
package index](https://pypi.org/project/haziris/) 

```sh
pip install haziris
```

### Google Charts
The package contains a number of wrapper python modules to create Google charts in an HTML file from a pandas data frame.

Here is an example for creating a Material bar chart

```py
import pandas as pd
import haziris as hz

df = pd.DataFrame([
    ['2014', 1000,  400, 200],
    ['2015', 1170,  460, 250],
    ['2016',  660, 1120, 300],
    ['2017', 1030,  540, 350]
  ],
  columns = ['Year', 'Sales', 'Expenses', 'Profit']
)

hz.google_material_bar_chart(df, "Google material bar.html", {'legned':'None'})
```

The examples folder, contains more such examples.
